---
layout: post
title: Local Models for AI Development
categories:
- Software Development
- Technology
- Programming
- AI
tags:
- agents
- agentic programming
image: "/assets/img/postMedia/AI_LocalModelDevelopment.png"
date: 2026-08-04 00:00 +0000
---
I am starting an investigation of how to use local models to substitute for cloud based AI coding agents such as Claude and Copilot CLIs. I am only at the start of this investigation but will report on what I find periodically to keep track of what I discover.

## Machine Specs Matter

First thing that has become apparent, and likely obvious, is that a beefy machine spec is needed for this. I had purchased a laptop with some very nice specs, including an NPU, but the fact is that the GPU VRAM memory is most important to the size and speed of model that a machine is capable of running.

Local models (as well as cloud ones) are qualified by the number of parameters they can handle. Smaller models that can do things like assist with emails, or rephrase and summarize text, are in the 7 billion range, noted as '7B'. These can even be used for the completion you see in VS of methods or single lines of code. While you need significantly larger models for more depth of knowledge coding challenges such as designing a new feature or refactoring of large sections of a code base.

## Model size to GPU VRAM

The correlation between model size and GPU VRAM is pretty linear. A GPU with 12GB of VRAM can run a 11B Model pretty successfully, and likely can run a step or two up from there, but at a much reduced speed.  Thus if you want to use the local model for complex feature changes in your code you'll likely need to have a 32GB or 48GB GPU to achieve the higher 32B or 70B models needed for this work.

There is [a very nice YouTube video](https://youtu.be/hfba9dAT6xE) that details the setup of Qwen models that also links to [a site detailing these model size to GPU](https://clever-mirage-d82v.here.now/) VRAM relationships.

## Apple M series 'Universal memory'

The newest Apple laptops boast an interesting option for what they call Universal memory. Apple silicon uses a shared pool of physical memory that can be accessed by both the CPU and GPU.

The issue here is a double‑edged sword. While an M‑series machine with large unified memory will definitely let you run a larger local model, its memory bandwidth (~300–500 GB/s depending on the chip) is significantly lower than the discrete VRAM on an NVIDIA GPU (typically 800–2,000 GB/s). So you can load a larger model, but the speed is not the same as if you had that same memory on a GPU. Still, the cost and convenience may be what brings you to the Mac devbox

Currently I'd advise a Mac only if your devs are into that ecosystem already, and pay more for a nice NVIDIA GPU if they are mainly on Windows/Linux.

## My Path

Since my current development box is Windows running on 12GB GPU, I've gone to the trouble of purchasing a PNY NVIDIA Quadro 6000 GPU (48GB) to test this out and will report back. I picked this GPU because NVIDIA is the main game in town for AI, and even their own current line does not go beyond 32GB. The PNY partner line has 48GB, and is roughly three-fifths the price of other models.

## Garage sale

On another note... if you are looking for a nice NVIDIA GTX 3080 (12GB), I'll be selling one... :)
