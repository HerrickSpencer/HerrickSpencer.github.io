---
layout: post
title: 'TOW: Vector memory allocation improvements in CPP'
categories:
- Tip Of The Week
- Programming
tags:
- Tip Of The Week
- cpp
date: 2024-10-30 00:00 +0000
image: /assets/img/postMedia/memory allocations hero.png
---
![TOW](/assets/img/postMedia/TipOfTheWeek.jpg){: width="200" .left}

Recently I was looking through some code and found a situation where we were converting IVector (WinRT) to std::vector and did so with a simple set of steps, declare the vector, then loop through the IVector items to push_back those items onto the std::vector.

But this got me thinking about all the allocations needed to do this. I was an O(N) efficiency of allocating new memory on the heap for each of these items. There had to be a better way when the number of items, and thus the final size of the memory allocation, was already known at the start.

## A better way

### Use vector.reserve()

Use vector.reserve() when the number of items to be inserted into a vector is a known quantity. This does one allocation of memory for all items rather than one allocation per push_back.

Instead of an allocation for each item in the loop, call vector.reserve( #of known items) to reserve the space ahead of time, allowing for the vector to allocate all the memory needed in one pass.

example:

``` cpp
std::vector<size_t> indexes;
indexes.reserve(m_annotations.size()); // This allocates all the known space needed.
for (auto& annotation : m_annotations)
{
    indexes.push_back(annotation.first); // no growth of vector size is needed
}
```

### Use emplace_back when possible

In the case of unnecessary copy calls, simply alter these to be emplace_back to use the constructor for the known type to assign the result directly to the memory space without a separate copy call of the object.

``` cpp
std::vector<OcrLineGroup> lineGroups;
lineGroups.reserve(lines.Size());
for (const auto& line : lines) {
-      lineGroups.push_back(OcrLineGroup(line)); // this creates an unnecessary copy
+     lineGroups.emplace_back(line); // this uses the constructor for OcrLineGroup and no extra copy
}
```

This has a major effect in performance... see details in experiment 2 here ['An In Depth Study of the STL Deque Container'](https://www.codeproject.com/Articles/5425/An-In-Depth-Study-of-the-STL-Deque-Container)

### Try to use std::array instead of std::vector

Next is trying to use std::array rather than std::vector. This is beneficial because array is allocated on the stack and vector on the heap. Stack memory is way faster.

When a vector's items are known and non-mutable, then simply use an array. If they are in a method that merely returns these values, you can make the change like so:

#### Before:

``` cpp
std::vector<std::pair<PatternType, std::wregex>> GetPatterns()
{
    std::vector<std::pair<PatternType, std::wregex>> patterns;
    patterns.reserve(12);
    patterns.emplace_back(PatternType::PhoneNumber, phoneNumberPattern1);
    patterns.emplace_back(PatternType::PhoneNumber, phoneNumberPattern2);
    patterns.emplace_back(PatternType::PhoneNumber, phoneNumberPattern3);
    patterns.emplace_back(PatternType::PhoneNumber, phoneNumberPattern4);
    patterns.emplace_back(PatternType::PhoneNumber, phoneNumberPattern5);
    patterns.emplace_back(PatternType::PhoneNumber, phoneNumberPattern6);
    patterns.emplace_back(PatternType::PhoneNumber, phoneNumberPattern7);
    patterns.emplace_back(PatternType::PhoneNumber, phoneNumberPattern8);
    patterns.emplace_back(PatternType::PhoneNumber, phoneNumberPattern9);
    patterns.emplace_back(PatternType::PhoneNumber, phoneNumberPattern10);
    patterns.emplace_back(PatternType::PhoneNumber, phoneNumberPattern11);
    patterns.emplace_back(PatternType::Email, emailPattern);
    return patterns;
}
```

#### After:

``` cpp
std::span<const std::pair<PatternType, std::wregex>> GetPatterns() {
 static const std::array<std::pair<PatternType, std::wregex>, 12> patterns = {
  std::make_pair(PatternType::PhoneNumber, phoneNumberPattern1),
  std::make_pair(PatternType::PhoneNumber, phoneNumberPattern2),
  std::make_pair(PatternType::PhoneNumber, phoneNumberPattern3),
  std::make_pair(PatternType::PhoneNumber, phoneNumberPattern4),
  std::make_pair(PatternType::PhoneNumber, phoneNumberPattern5),
  std::make_pair(PatternType::PhoneNumber, phoneNumberPattern6),
  std::make_pair(PatternType::PhoneNumber, phoneNumberPattern7),
  std::make_pair(PatternType::PhoneNumber, phoneNumberPattern8),
  std::make_pair(PatternType::PhoneNumber, phoneNumberPattern9),
  std::make_pair(PatternType::PhoneNumber, phoneNumberPattern10),
  std::make_pair(PatternType::PhoneNumber, phoneNumberPattern11),
  std::make_pair(PatternType::Email, emailPattern)
 };
 return std::span<const std::pair<PatternType, std::wregex>>(patterns);
}
```

This later example uses span to return the static const array. The reason it does not simply return an array like so:
``` std::array<std::pair<PatternType, std::wregex>, 12> ```
is to allow for future additions to the array without having to change code downstream that is expecting 12 items. By returning a span, the downstream code has to expect N items.

## Conclusion

Memory management in CPP is hard enough... but looking for these type of allocation improvements is not too hard. Check through your own code to see if you've got any array/vector situations where the items to be allocated are already know prior to the declaration. There code be a place for you to use the steps in this post to make improvements.

Happy coding!
