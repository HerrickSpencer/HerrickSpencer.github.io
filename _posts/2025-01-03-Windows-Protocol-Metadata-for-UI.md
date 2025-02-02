---
layout: post
title: "TOW: Protocol launch button that keeps icon/appname updated!"
categories:
  - Programming
tags:
  - protocol
  - UI
  - UWP
  - WinUI
  - XAML
image: /assets/img/postMedia/ProtocolMetadataButton.png
date: 2025-02-03 00:00 +0000
---
![TOW](/assets/img/postMedia/TipOfTheWeek.jpg){: width="200" .left}

In Windows applications, a protocol launch refers to the process of starting an application using a custom URI scheme. This allows apps to be launched from a URL or a link, similar to how `http://` or `mailto:` schemes work. There are so many apps, both Inbox to Windows and external third party apps, that come with protocol launch abilities.

A user however, can choose to change the app that is used to handle a particular protocol. For instance, `mailto:` could be Outlook or Gmail. Even established protocols can be overridden by another app, such as `ms-paint` launching another custom image editor, like gimp. (but you'd never use anything other than paint, now would you...)

![Default protocol settings](/assets/img/postMedia/ProtocolChangeSettings.png)

If you wish to have a button in your UI that will launch another app, perhaps with parameters to open the file your app is working with, there is the chance that the user has chosen another app other than the one you expected. Following is a great way to get the name and icon of that app that is chosen by the user to handle that protocol. You can then use this information in your app to set the image and tooltip of your button.

I'm using Calculator for an example here:
![Protocol Metadata Button](/assets/img/postMedia/ProtocolMetadataButton.png){: width="100"}
### Button Xaml
``` xaml
<Button x:Name="myButton" Click="myButton_Click">
	<StackPanel>
		<TextBlock x:Name="buttonText">ClickMe</TextBlock>
		<Viewbox>
			<Image x:Name="ProtocolButtonImage" />
			<!--  This is the icon loaded from the metadata!  -->
		</Viewbox>
	</StackPanel>
	<ToolTipService.ToolTip>
		<ToolTip x:Name="buttonToolTip" Visibility="Collapsed">
			<StackPanel>
				<!--  This is the display name loaded from the metadata!  -->
				<TextBlock x:Name="buttonToolTipText" />
			</StackPanel>
		</ToolTip>
	</ToolTipService.ToolTip>
</Button>
```

### Get the metadata for the protocol to use in the button
#### Class to hold the display name and icon
``` cs
public class ProtocolHandlerInfo
{
	public string DisplayName { get; set; }
	public SoftwareBitmap Logo { get; set; }

	public ProtocolHandlerInfo(string displayName, SoftwareBitmap logo)
	{
		DisplayName = displayName;
		Logo = logo;
	}
}
```
#### Get the metadata for a protocol, return the info (or null)
```
public static async Task<ProtocolHandlerInfo?> GetProtocolHandlerInfoAsync(string url, Size logoSize)
{
	var uriSchemeHandlers = await Launcher.FindUriSchemeHandlersAsync(url);
	if (uriSchemeHandlers.Count == 0)
	{
		// No handler found
		return null;
	}

	// Get the first, ignore the rest
	var uriSchemeHandler = uriSchemeHandlers.First();

	// Get display info
	var displayInfo = uriSchemeHandler.DisplayInfo;

	// Get the display name
	string displayName = displayInfo.DisplayName;

	// Get the logo
	SoftwareBitmap? logoBitmap = null;
	{
		var random = displayInfo.GetLogo(logoSize);
		var logoStream = await random.OpenReadAsync();
		var decoder = await BitmapDecoder.CreateAsync(logoStream);
		var tempBitmap = await decoder.GetSoftwareBitmapAsync();

		// Convert the alpha mode to premultiplied.
		// GetLogo() returns a bitmap with BitmapAlphaMode.Straight
		logoBitmap = SoftwareBitmap.Convert(tempBitmap, tempBitmap.BitmapPixelFormat, BitmapAlphaMode.Premultiplied);

		logoStream.Dispose();
	}

	return new ProtocolHandlerInfo(displayName, logoBitmap);
}
```
### Load meta data and add to the button
``` cs
private async void LoadButtonData()
{
	ProtocolHandlerInfo? handlerInfo = await ProtocolHelper.GetProtocolHandlerInfoAsync(protoUrl, new Size(100, 100));
	if (handlerInfo != null)
	{
		buttonText.Text = handlerInfo.DisplayName;
		buttonToolTipText.Text = handlerInfo.DisplayName;

		Microsoft.UI.Xaml.Media.Imaging.SoftwareBitmapSource bitmapSource = new Microsoft.UI.Xaml.Media.Imaging.SoftwareBitmapSource();
		await bitmapSource.SetBitmapAsync(handlerInfo.Logo);

		double scale = this.Content.XamlRoot.RasterizationScale;
		ProtocolButtonImage.Width = (handlerInfo.Logo.PixelWidth / scale);
		ProtocolButtonImage.Height = (handlerInfo.Logo.PixelHeight / scale);

		ProtocolButtonImage.Source = bitmapSource;

		buttonToolTip.Visibility = Visibility.Visible;
		buttonText.Visibility = Visibility.Collapsed;
	}
	else
	{
		buttonText.Text = "No handler found";
	}
}
```


Now you can create a button that automatically updates the icon for your protocol when the icon for that app is updated, or the default app that handles that protocol is changed.

Enjoy!
