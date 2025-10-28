---
layout: post
title: "TOW: AI Task Flow Demonstration with GitHub CoPilot"
categories:
  - Programming
tags:
  - AI
  - CoPilot
  - GitHub
  - Visual Studio
  - Visual Studio Code
  - VS Code
  - prompt engineering
image: /assets/img/postMedia/ProtocolMetadataButton.png
date: 2025-02-03 00:00 +0000
---
![TOW](/assets/img/postMedia/TipOfTheWeek.jpg){: width="200" .left}

## AI Task Flow Demonstration with GitHub Copilot

AKA: _AI Prompt-inception_

## Introduction

- Brief overview of the AI task flow concept
- Importance of improved AI-assisted coding workflows
- Key Features of the AI Task Flow

## Many different flavors of this flow available

We will be using one I found and like called [<span style='font-size:22'>ai-dev-tasks</span>](https://github.com/snarktank/ai-dev-tasks) by:  
**Ryan Carson (gh:snarktank)**  
_CEO, Founder, Dev._  
_Built and sold 3 startups._  

- DropSend (to AWS)
- Treehouse (edu)
- Maple (AI edu)
- Untangle (Conn divorce assist)
- Builder in Residence, Amp.

> Note: I have modified my version of the prompts to meet the needs of me and my team. You should do the same.

## Basic High-level flow

![AI Task Flow diagram](/assets/img/postMedia/AI%20Task%20Flow/AI%20Task%20Flow.png)

## Multi-step, interactive code changes vs. single prompt edits

<table>
<tr>
<td colspan=2>The multi step flow at first seems longer... but results in fewer iterations for changes due to confusion (by the AI) and results in way more documentation such as a full spec and dev plan. There is more maintainability overall with  clarity of the changes.</td>
</tr>
<tr>
<td style="width:50%; vertical-align:top; text-align:center; padding-right:10px;">

![Single step flow](/assets/img/postMedia/AI%20Task%20Flow/Single%20Flow.png)</td>
<td style="width:50%; vertical-align:top; text-align:center; padding-right:10px;">

![Multi step flow](/assets/img/postMedia/AI%20Task%20Flow/Multi%20Flow.png)

</td>
</tr>
</table>

Single Prompt | AI Spec Task Flow
-- | --
Messy results with little oversight, lots of things for the user to correct on initial response | Works with a detailed list of tasks that meet the spec requirements and are approved ahead of time. Less dev cycles
Very large set of changes on first iteration that is hard to review | Many small sets of commits for each and every step of the tasks that are atomic in nature and easy to review and alter along the way
Monolithic PRs that are hard to understand and review | Each set of tasks can be submitted separately, cohesive understanding for reviewers.

## Self-documentation capabilities

Every step of the way this flow creates documentation vital to maintainability. 

1. From the start the feature is well documented by the collaboration of the Users AI and the AI generating a Dev Spec (PRD).
2. This is then used as input to the next phase, creating an actionable list of tasks.
3. At any time in the flow, a set of diagrams (markdown mermaid flow and class diagrams) can be asked for and generated for better readability by the team.
4. git commit messages self document each step checked in
5. PR descriptions can be made part of the flow for final review by the team

## Role of the AI as a coach and peer reviewer

This system adds much more flexibility for user questions and suggestions all throughout the process, allowing the dev to act as a coach to a very smart junior dev as they tackle a large scale change. This is contrasted by the fire-and-forget nature of the single prompt flow that ends in messy conversation and lack of clarity.

## Demonstration Plan

- Show a simple code change using traditional single prompt approach
- Contrast with the AI task flow multi-step approach
- Highlight how documentation updates automatically
- Demonstrate mid-process plan changes based on user input

## Benefits and Improvements

- Increased reliability and clarity in code changes
- Enhanced collaboration between user and AI
- Better adaptability to evolving requirements

## Conclusion

- Summary of key takeaways
- Encouragement to try the AI task flow approach
- Open floor for questions and feedback
