---
layout: post
title: Cut AI Credit Usage by 5–20× Without Losing Productivity
categories:
- Software Development
- Technology
- Programming
- AI
tags:
- agents
- agentic programming
image: "/assets/img/postMedia/AI_TokenUsageReduction.png"
date: 2026-08-07 00:00 +0000
---
## Introduction

*The problem:* AI credit burn is real, especially with frontier models. Since the change in pricing models from a ‘all you can eat buffet’ to a per token or per ‘AI Credit’ plan, there has been a huge worry that the costs of using AI for every task will outweigh the benefits.

I recently tracked my usage over a month of unlimited usage in April and found that with the current pricing models it would have cost me $5,000. Luckily my company owns the LLM and Agent… and licenses the model I was using (Opus 4.6 mainly) and I didn’t pay a dime.

*Why this matters for developers, teams, and power users.* The days of your company allowing you to spend freely in AI credits are numbered, and likely to meet a policy shift to prioritize using certain models for specific tasks, or even not using AI at all where the task has lower ROI than the engineer performing it ‘old-school’.

Using 3x or more models for simple tasks is just not needed if you are doing simple method collaborating or targeted changes that any engineer can accomplish. However, large to medium feature or refactoring benefits from AI Collaboration in the planning phase, and likely in implementation if the change is fully defined and well designed prior to execution. The trick is to minimize the context along the way.

Quick promise: simple workflow changes can reduce spend dramatically. I am a big proponent of using AI to collaborate on design. Having a ‘junior engineer’ that knows all of the design patterns better than I, has read all the framework documentation, and has instant access to all questions asked on coding forums, is definitely going to be an asset in complex feature change conversations. I act simply as a guide to ‘steer’ the AI in the direction I feel is best based on a decade of experience.

One of the better strategies is to split the work flow into planning, designing, and staged implementation. This nicely follows stage 6 of [The 7 Stages of Vibe Coding]({% post_url 2025-11-03-the-7-stages-of-vibe-coding %}).  If you indexed your code properly the context to the planning phase can be quite light, and that conversation should take the longest of all the other phases. Each phase should end with a summarized document used in the next phase. This keeps the context very low, and thus costs as well.

## The Core Idea: Use the Right Model for the Right Job

### Strategic Model Usage

The cost differences between Opus, Sonnet, and Haiku / mini models are pretty stark, so using them strategically may game the system better.

|Model|Cost per 1K Tokens (Prompt / Completion)|Best Use Cases|
|---|---|---|
|Opus|\$5 / $25|Complex reasoning, deep research, multi-step problem solving, large context tasks like codebase analysis and legal documents. Use when accuracy and depth matter.|
|Sonnet|\$3 / $15|General purpose coding, writing, analysis, multi-step workflows, customer support chatbots, and most production workloads.|
|Haiku|\$1 / $5|Fast, high-volume tasks, simple Q&A, quick summaries, classification, and extraction tasks where speed and cost efficiency are priorities.|

Opus is the flagship model designed for "think hard" tasks that require deep understanding and reasoning. It is not cost-effective for boilerplate or simple tasks.

Sonnet is the versatile daily driver, balancing cost and capability for most coding and content creation tasks.

Haiku (and mini models) are optimized for speed and volume, ideal for straightforward, high-frequency tasks.

Use this tiered approach to optimize AI credit usage by matching task complexity to the appropriate model

### Additional Notes on GPT-5 Models and Costs

|Model|Cost per 1K Tokens (Prompt / Completion)|Best Use Cases|
|---|---|---|
|GPT-5.5|"$5.00 / $30.00"|Advanced coding, professional work, complex reasoning, multi-step problem solving. Use when highest accuracy and depth are required.|
|GPT-5.4|\$2.50 / $15.00|Coding, professional work, general purpose tasks with good balance of cost and capability.|
|GPT-5.4 mini|\$0.75 / $4.50|Coding, computer use, subagents, smaller scale tasks needing efficiency.|
|GPT-5 (default)|\$1.25 / $10.00|Coding, reasoning, agentic tasks, general purpose AI tasks. Good balance of speed and accuracy.|

GPT-5 models are priced per million tokens, which is a much larger scale than the Claude models priced per thousand tokens.

GPT-5 mini and nano models offer lower-cost options for less complex tasks.

GPT-5 models are suitable for a wide range of tasks from coding to complex reasoning, with the highest-end models reserved for the most demanding workloads.

Summary

Claude models (Opus, Sonnet, Haiku) are priced per 1,000 tokens and are tiered for complexity and cost efficiency.

GPT-5 models are priced per 1,000,000 tokens and offer a range of options from high-end to mini and nano for cost-effective usage.

Use Opus or GPT-5.5 for deep, complex tasks requiring accuracy.

Use Sonnet or GPT-5.4 for general purpose coding and writing.

Use Haiku or GPT-5 mini for fast, high-volume, or simpler tasks.

This tiered approach helps optimize AI credit usage by matching task complexity to the right model, balancing cost and performance.

## Avoid Huge Context Windows

### Why large prompts = large bills

Examples of expensive patterns are submitting a search across whole repos, giant logs, and massive diffs.

Better alternatives: scoped file prompts, trimmed logs, targeted diffs.

This can be achieved in various ways. one is by using MCP servers that index the codebase. Provide tools that allow the LLM to quickly find information regarding the codebase, such as detailing how it is segmented and what source builds what binaries.

This allows a reduced context but maintains ability to grok an entire codebase without actually reading it in detail. Thus reducing your input token costs.

### Output verbosity = unchecked costs

Another side of the literal coin is the output from the LLM that can drone on and on in long verbose explanations. The returned response is less in our control, but still comes with a cost.

Verbose LLM responses burn output tokens, which are often 2–5× more expensive than input tokens on frontier models.

I'm sure there may be other ways, but the only one I've found is adding instructions to reduce this tendency for long winded 'help'. Add to the .github/copilot-instructions.md or Claude.md instructions to minimize output response from the LLM.

Adding instructions like:
> “Be concise”
“No explanations”
“Code only”
“Return JSON only”
“Avoid commentary”

does reduce output tokens, often saving 200–500 tokens per response. However, it likely is something largely out of our control, with context bloat being a larger cost.

## Disable Agentic Behavior When You Don’t Need It

Hidden costs: recursive planning, retries, repo scans.

Cheaper alternatives:
> “Summarize likely causes”
“Suggest minimal fix”
“Generate patch only”

### Prefer Iterative Edits Over Full Rewrites

Output tokens matter more than people think.
Example: “Rewrite this file” vs. “Modify only the retry logic.”

- Keep Conversation Threads Short
- Long chats accumulate hidden context.
- Starting fresh reduces token load.
Use /new or equivalent CLI commands.
- Avoid Verbose Outputs
“Explain every step” = expensive.
- Encourage concise prompts:
>“Root cause + minimal fix”
“Patch only, no explanation”
- Use Local Tools First that replace expensive AI calls:
> grep / rg
fd
jq
git blame
build

Any git command should be done independent of AI if possible.
Have AI write or make scripts for repeatable actions (restarting services or test scripts)

## Watch Out for Auto Model Selection

“Auto” can escalate to expensive models.
Recommendation: pin cheaper models by default.

Use lower level models for menial tasks like documentation or simple method creations in an IDE.

### High-Leverage Prompt Constraints

Add constraints like:
> “<200 words”
“Patch only”
“One solution only”

Constraints reduce chain depth and output tokens.

## A Practical Tiered Strategy (Recommended Setup)

Haiku/mini/GPT → grep-like questions, tests, docs

Sonnet → daily driver for coding + PRs

Opus → architecture, debugging, multi-file reasoning

## Expected Results

Typical improvement: 5–20× reduction in AI credit usage. *[based on non-scientific evidence by this developer/author]*

Realistic expectations for power users may be different (YMMV) and an evolution of procedures and policies overtime will result in new incites only if there is a way to evaluate ROI of AI usage. 

Some teams have worked on AI Usage per PR count, which in my opinion is slightly flawed, but still a useful metric. Others have made this more specific by looking at lines changed, or features/tasks completed. I'd advise caution in using any of this for performance metrics of employees, and keeping is solely as a way to improve AI Collaborative efficiency.

## Conclusion

I encourage readers to experiment with model tiering and scoped prompts. Look into ways to limit context in prompting, such as utilizing MCP tools (either homegrown or purchased/shared) that will give the LLM best chance at understanding codebases and problem scope without scanning entire repos.

With this combined with possible [Local model options]({% post_url 2026-08-04-Local-Model-AI-Dev %}), it is possible to greatly reduce costs of development with the new subscription models AI providers are presenting.

Good luck!

Notes/Sources:
[Microsoft CEO Satya Nadella Warns Against AI Overuse - don't use frontier models for non-frontier problems](https://www.msn.com/en-us/money/general/microsoft-ceo-satya-nadella-warns-against-ai-overuse-don-t-use-frontier-models-for-non-frontier-problems/ar-AA25nA0d?ocid=BingNewsVerp)
