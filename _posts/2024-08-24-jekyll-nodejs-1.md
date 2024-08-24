---
layout: post
title: Jekyll sites with Node and ExpressJS to Authenticate users! (Part 1)
categories:
- Programming
tags:
- websites
- nodeJS
- expressJS
- Jekyll
- Chirpy
excerpt: Have you ever wanted a bit more from your Jekyll static site? Something like
  adding authentication or database serving data to certain pages? Join my adventure
  to learn how.
image: "/assets/img/postMedia/JekyllWithNodeJS.png"
date: 2024-08-24 12:36 -0700
---
Have you ever wanted a bit more from your Jekyll static site?

- Something like adding authentication or database serving data to certain pages?
- Maybe you want to have a sign-in for some sections of the jekyll served pages, and allow others to be open to all?
- Maybe you want the static site to just be a subset of the overall site that is not static? IE: supporting marketplace activities, or gathering comments, or other post behaviors.

## My requirements

Well this is just what I wanted for the latest project that my brother and I are working on. We wanted to create a post like site with stories from our families, and be able to use the nice style rich controls that Jekyll offers in the static generated site, but also wanted to both secure it to only to family members (or close friends), as well as allow members to add their own posts, comments and stories to the mix.

## My Plan

My search led me to a NodeJS/ExpressJS site using MongoDB, Express-Sessions, Passport-Local(or other flavors), and JWT for sustaining login.

In [Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy#documentation) (and lots of Jekyll themes) the *_site* folder is used to hold the statically generated pages. My goal was to serve these up from a NodeJS site similarly to how I'd assumed my GithubPages server was doing the same thing.

The first stage in this is to prove that I could serve the *_site* folder that is generated from my [Chirpy themed blog](https://github.com/cotes2020/jekyll-theme-chirpy#documentation).

## Journey thus far

Steps:

1. I installed Node Version Manager (NVM)
   1. ``` winget install "NVM for Windows" ```
2. I used that to install the latest node version
   1. ``` nvm install lts ```
3. I started a new ExpressJS site locally with a simple app.mjs file to start.
   1. This requires adding express
      1. ``` npm install express ```
4. I got this serving simple content from simple routes just to prove it was operating correctly on the local machine.

    ``` javascript
    import express from 'express';

    const app = express();

    app.get('/', (req, res) => {
        res.send('Hello, World!');
        console.log('Hello, World!');
    });

    app.listen(3000, () => {});
    ```

5. Then after that was working I copied the *_site* folder from my other repo for this very blog over to this folder to test if I could serve all the pages using proper routes.

    ``` javascript
    import express from 'express';
    import { get } from 'http';
    import { join } from 'path';

    const app = express();

    function getIndex(req, res) {
        const filePath = join(process.cwd(), 'src', '_site', req.url, 'index.html');
        res.status(200).set('Content-Type', 'text/html').sendFile(filePath);
        console.log('base: ' + req.url);
    };

    app.get('/', getIndex);
    app.get('/Categories', getIndex);
    app.get('/Tags', getIndex);
    app.get('/Archives', getIndex);
    app.get('/posts/*', getIndex);

    app.listen(3000, () => {console.log('Server is running on http://localhost:3000/')});
    ```

6. Why the getIndex function?
   1. At first I'd made app.get routes for each of the different areas... but realized that jekyll (or Chirpy) was just creating content for each of the posts and tabs under a folder for that section, with a separate index.html for each. Example, the page for this post will be under a separate folder found at *_site/posts/[title of the page]/index.html*.  This allowed me to set a function to handle all of those routes as just pointing at the index.html under the request set to the server.
7. Static content failing
   1. Next I realized that all the static content of the site was failing, things like images, css files, and javascript files that supported the search box, comments, and page views. This made the site look rather horrible.
   2. The answer was to add a middleware use for express.static to serve all these items, as they were all called by the *assets* folder, we could solve them all at once. Creating a virtual *assets* folder was the answer, putting this at the top before all other routes helped make sure it didn't get re-routed later.

      ```javascript
      app.use('/assets', express.static(join(process.cwd(), 'src', '_site', 'assets')));
      ```

## Success

And it works!  
Next I'll be trying to add the sign-in and authentication portions of the express site, as well as a middle ware for restricting access to all the posts and images served to them to protect privacy of our family.

I'll keep you posted on the progress!
