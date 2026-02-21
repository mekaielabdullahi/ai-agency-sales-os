# Meeting Transcript - Chris Fireflies Integration

**Date:** December 29, 2025
**Recording:** [Fathom Recording](https://fathom.video/share/FAR87xKdceD-xoqqchGFvu-xnAUJ5qM2)

---

## Transcript

Impromptu Google Meet Meeting - December 29
VIEW RECORDING - 96 mins (No highlights): https://fathom.video/share/FAR87xKdceD-xoqqchGFvu-xnAUJ5qM2

---

0:00 - Matthew Kerns (12kernsmatthew@gmail.com)
Like, I was on a walk and using the Cloud Code OS mobily on my Cloud app, on the mobile app, and basically, like, I talked with it for a good, like, 10-15 minutes, and I was out there, and then, like, I checked back in with it again, I closed it out, and stuff. Actually, I didn't, like, exit the app or anything, but when I came back, it was gone, it was, like, the whole thread was kind of, like, gone, so that, I was just saying that happens sometimes, it doesn't happen a lot, but it happens, like, you know, every once in a while, but, yeah, we shouldn't get discouraged, like, I do get discouraged every time, because I'm like, man, I must, I, like, lost some good stuff, you know, but what I do, what I try to do is just just say all the stuff again, like, literally just suck it up, and, like, just five minutes, just say when And like, basically, I'll just fill it in. And, you know, it happens so few and far between that it shouldn't happen twice in a row. So it should, like, be fine now. But yeah, I just want to let you know that that can happen sometimes. So just don't panic.

1:19 - Chris Andrade
Yes, that has happened with, with Gemini. Okay. So, yep. That's why I started documenting when I started messing around with workbook one. I'm very diligent, like how I talked. And then when before I move forward, I have this process. Okay, did I update? But I had to make sure all the documents were updated too. Did it go here? Did it go here? know?

1:56 - Matthew Kerns (12kernsmatthew@gmail.com)
Yep. Because that's what I was afraid of.

1:57 - Chris Andrade
And I didn't want to have to re- So one of my biggest pet peeves is I hate doing things twice Yeah, yeah, I don't like it.

2:12 - Matthew Kerns (12kernsmatthew@gmail.com)
Serious pet peeves of mine, so I make sure that does not happen Yeah, so quick story on that for me, like early on in my coding career when I was in college, it was like one of the first projects, I did all this work on this coding project, and it was like operating systems class, it was like the upper division, like, like, holy crap, this is hard, this is difficult, and worked on it for like 10 hours, like several hours, right? And I lost the whole thing, like, something happened, I don't know what happened, it got deleted. And I was just like, well, , like, it's due in like three days, I'm gonna have to rebuild anyways, I might as well just start now. And I'm gonna Literally, I rebuilt it to where it was within like, within two hours. And I was like, oh my gosh, you know, it was a revelation. It was like, I've already thought through it all, right? I've already been through the hurdles, know, when I, when I do it again, it's going to go faster. And it did.

3:23 - Chris Andrade
So that was my learning, but yeah, no, I like that. Because it's exactly, I mean, discouragement, like these valleys, like, I'll be honest, these valleys of despair, they will eat you alive. And I, that's why I love our group, because I feel that we help push each other out of those valleys. Like, I, I honestly, I couldn't even think this was possible without any of you guys, let alone Bob Knight. Right? And like, just the fact that because I do get discouraged easily, but the fact that you guys make it so hard, because I didn't say that saying like, it's too good to be true. And nine times out of 10 for like, oh, it's always been too good to be true straight up like I haven't had a tank, you know, maybe I this is 10. Like I really truly feel that. Yeah. So I think so too.

4:37 - Matthew Kerns (12kernsmatthew@gmail.com)
But yeah, we'll got to make it happen. At the end of the day, right?

4:40 - Chris Andrade
Like what we're doing right now, bro, is this is like this. So my, my kids, they were going bullying. They're like, Dad, come with me. And it was like, Listen, I'm sacrificing because this is so important. Like once I get this live, like this iteration, so I got the database built, it's already going. I bought credits, and I'm now connecting my Fireflies to my, I don't know if I'm doing it right, so before I do anything, can I show you before, like, so this is where I'm at, right?

5:19 - Matthew Kerns (12kernsmatthew@gmail.com)
What are you doing?

5:21 - Chris Andrade
So I, after I've pushed, right, so now the OS has been, is live on GitHub?

5:35 - Matthew Kerns (12kernsmatthew@gmail.com)
Oh, yeah. Hell yeah.

5:38 - Chris Andrade
So then I said, and then right now when we called, my Fireflies is an issue, again, because I do. So then I started working that problem, I was like, now, honestly, I'm looking back, I already have AZ events, I already have the shoe store. And my fireflies that still needs to be processed, right? And then I have another Maples apothecary going to call me in the next two hours. Okay, sweet. So we're going to get that number that three that my goal was last night. Those are already been filled. So I already made this week's goal for the opportunity calls. We already technically have one opportunity call done with the shoe. Because I already went through the questions. That's what I have here on my fireflies. We can get that opportunity matrix done by this week. So we can have one opportunity matrix for the shoe store. We can have another opportunity matrix for S&S woolsheds. We have another opportunity matrix for AZ events. We still need AZ introduce.- It's discovery call. Then we have an opportunity and a discovery call for Maples Apothecary. Wow.

7:11 - Matthew Kerns (12kernsmatthew@gmail.com)
That's full this week.

7:13 - Chris Andrade
Sounds like I need to get a haircut today.

7:15 - Matthew Kerns (12kernsmatthew@gmail.com)
So I look good on these calls.

7:18 - Chris Andrade
Yeah, I mean, that's why I shorted my I got I shorted my up a little bit, you know, treated up a little bit. So I did. But now. So now I was like, I need to connect my fireflies because this is where it all starts for me right here. So I think, well, I see I already got all my I see I have this API key here. I was like, well, what happens? So then I moved over here. So I was like, I need to connect my fireflies to pull meetings from. Yep. And then it's how do you want to integrate? And I said API integration, right? Yeah.

7:58 - Matthew Kerns (12kernsmatthew@gmail.com)
Okay. month capture the It's Thank you.

8:00 - Chris Andrade
and then it says got it api integration let me look at fireflies api web search authentication so it says it fetched this document fireflies api that gives you access to full transcript speaker attribution summaries action items key let me first let me set this up first where should meeting data live live on your os and so it's asking what do i want this firefly means to be stored uh definitely not the first two uh i think so where i have mine is in is in operations but what i'm let me know what you think about this so i already have a setup in mine maybe

9:00 - Matthew Kerns (12kernsmatthew@gmail.com)
Maybe you build out yours the way you want it. Maybe that's better. But I was just thinking like I have a setup in my agency development OS that has like meetings. Basically, there's in operations, there's a project management folder, and then there's a active projects folder. And then there's a discovery process with agents that run the initial discovery output opportunity matrix and process. So I'm thinking you can, you can just have it, your GitHub account already has access to that repository. So we can just tell it like, can you grab the structure from this repository and do that? I love that plan.

9:45 - Chris Andrade
I would I would like to mimic you as much as possible. If that makes sense.

9:52 - Matthew Kerns (12kernsmatthew@gmail.com)
Okay. Yeah, and then I think we should do that. There's probably some stuff from Mikael's OS. say, know. So I know you mentioned before about you getting up to speed on something I just feel like sooner I can like okay now I take my audio file up I can just designate it to my fireflies all if I could just funnel everything through there and then just start breaking it down from there and understanding it from there it would alleviate a lot of my downloading, implementing, and running you know what mean yeah we also got to get you up on Trent's workspace but so a lot of these process map stuff by the way I pulled from work that Mikhail had done on opportunity matrix and all that stuff so but yeah just check out the go to the google meet chat and I posted the link to my github Repository. So yeah, you got it. So just copy and paste the link, like the URL, and then let's say, let's think of how to prompt this. So in your VS code, let's go down to type something and then so there, you can say something like there's already a structure in this repository, and then you paste the link or yeah. Kind of like build out. A project management structure plus meeting folder structure for discovery calls. I would also say project management structure inside the operations, inside O2 operations.

12:35 - Chris Andrade
So yeah, so I should say pop the O2 operation folder structure.

12:43 - Matthew Kerns (12kernsmatthew@gmail.com)
I don't, I guess you could, but there's some stuff, yeah, I mean, that might take a while. kind of wanted to just focus on the project management and meeting. Let's go. Thank Project management, oops, and yeah, that's good. That's good. And meeting structure. I would just say focus on the project management and meeting.

13:23 - Chris Andrade
I already got meeting folder structure, project management folder structure.

13:28 - Matthew Kerns (12kernsmatthew@gmail.com)
So wait, so you said, yeah, just go erase that, that period, the end of that sentence, the period at the end there. So you can just like.

13:39 - Chris Andrade
Oh, yeah. Okay. Yeah.

13:43 - Matthew Kerns (12kernsmatthew@gmail.com)
And then just say, and instead of the period. Build out my meeting folder and project management structure inside 02 dash operations is important. So of Okay. Yeah. Okay, through and get a of Okay, so, Okay,

14:04 - Chris Andrade
Like that? Yeah, dash operations.

14:10 - Matthew Kerns (12kernsmatthew@gmail.com)
Oh, 02, 02 dash. Yeah. And then one zero, yeah. I think that's what we want. Let's see. And then you can kind of tie it to the Fireflies thing. So just say, like, this is where we'll store Fireflies meeting summaries and transcripts. That's what we're let's see. The Fireflies coming in. I'm Thank Meeting, put summaries also, summaries and transcripts, because then it'll pull that, the way I do it and mine. So I think this is good for now. Oh wait, you got to type, put the, paste the link too.

15:38 - Chris Andrade
Oh yeah, thank you. Thank you. Yep.

15:43 - Matthew Kerns (12kernsmatthew@gmail.com)
Okay.

15:45 - Chris Andrade
Leave it as is. Yeah.

15:49 - Matthew Kerns (12kernsmatthew@gmail.com)
What do you think about this prompt? Is this good? This is, there is a structure in the repository. Typos and stuff are fine, by the way.

16:09 - Chris Andrade
To reference venues to build out my meeting folder structure and project management structure inside O2 operation folder structure. This is where we will store the fireflies meeting summaries. Yeah? Do you want to pull from each meeting full package, summaries, full transcripts?

16:40 - Matthew Kerns (12kernsmatthew@gmail.com)
Yeah, all the context, full package, I would say.

16:46 - Chris Andrade
Where should the firefly, okay, got it, full package, submit answers. Sweet.

16:56 - Matthew Kerns (12kernsmatthew@gmail.com)
I was probably going to ask to web search or something, you have to approve. you. you. Thank you. you. Maybe. Let me take a look. There you go. I would say don't ask again for ghapi commands. So it'll just do it. Same thing for this one. It'll figure it out. Yep. There we go. I had to use it. Yeah. Yeah, yeah, yeah. I had to use the right tool. had to figure out. Okay. I tried this. Didn't work.

17:56 - Chris Andrade
That's crazy.

17:58 - Matthew Kerns (12kernsmatthew@gmail.com)
Yeah. So. Thank you all.

18:00 - Chris Andrade
With just a number one, I would do number two.

18:04 - Matthew Kerns (12kernsmatthew@gmail.com)
So it'll just web search for you. Yeah, don't make sure.

18:08 - Chris Andrade
Yep.

18:13 - Matthew Kerns (12kernsmatthew@gmail.com)
Otherwise, it'll ask you every time if it wants to do a web search.

18:18 - Chris Andrade
But yeah, okay, this is tremendously like if dude, we have another four discovery phone calls or four opportunity matrix and we send out this week. Yeah.

18:33 - Matthew Kerns (12kernsmatthew@gmail.com)
No, I don't.

18:37 - Chris Andrade
I know. I don't know what Maples apothecary might be more of a practice run because they don't have a bunch of funds. Just design the meeting structure for me. So it's asking.

18:55 - Matthew Kerns (12kernsmatthew@gmail.com)
It's it's saying it can't access. Tell it my aid. Tell it my Github account has access to this repository Yeah, it should try and go through the Github API now. Which I thought it did before, but let's see what happens Yeah, that's good. It's going to clone it onto your computer Oh, sweet.

19:43 - Chris Andrade
Which will then also be pulled to MyOS, which is where MyOS pulls from when I do it. From my phone? Right. Thank

20:00 - Matthew Kerns (12kernsmatthew@gmail.com)
No, so hit yes, and I'll tell you the answer to that. So it will now be stored on your computer in a separate workspace. So when you're on your computer, you can tell it like, hey, look at the development OS. It will only have that copy, like today's copy of my OS until you update it. So if you want the updated one, you're going to have to tell it, hey, can you get the updated version? And then...

20:29 - Chris Andrade
The updated version of what exactly? Of my development OS.

20:35 - Matthew Kerns (12kernsmatthew@gmail.com)
Oh, gotcha, gotcha, gotcha, gotcha.

20:38 - Chris Andrade
I see. Okay.

20:39 - Matthew Kerns (12kernsmatthew@gmail.com)
It doesn't like stay updated on your computer, like... No, no, I see what you're saying.

20:44 - Chris Andrade
No, I'm talking about referring to where the meeting notes live, or the transcripts. Those live on my local computer.

21:05 - Matthew Kerns (12kernsmatthew@gmail.com)
So hit yes, and then let's see, so the meeting notes and stuff, right now you're building the Fireflies integration, making sure the folder structure is there, and then, yeah. So it'll be in your OS, it'll be, you're going to pull it into your OS, and I need to do the same thing, I need to do this for my Fathom one. I don't think it will happen automatically yet, like I think you'll have to prompt it and be like, hey, I just had a meeting, can you pull notes in? But you might, once you set up this integration, you might be able to do it from the phone, I don't know how that works, but we'll test it out. But that's what it means. Yeah.

22:00 - Chris Andrade
So thinking is because I already have my fireflies that I can, like, I can just, that's how sometimes I'll just start recording myself to my own fireflies, right? Yeah. And then if I do that, instead of recording it to my microphone, and just get in the habit of talking to this, or have this Bluetooth to this, which Kelsey would do, and then automatically creating that firefly boom, you know, and then from here, these two fireflies, then I can access it. To get pulled to my environment, right?

22:44 - Matthew Kerns (12kernsmatthew@gmail.com)
Yeah, yeah, like as long as it gets stored somewhere. So once you have the audio file, whether it's through fireflies or your device, it's stored somewhere, and then we can, we can access it, we just need to pull it. And then that's the manual sort of way. And then we'll be able to automate it as soon as we can prioritize.

23:06 - Chris Andrade
Then after we get the integration going of what we're doing, once I can start uploading audio files, I can even start the opportunity matrix or pushing it through the opportunity matrix for you guys, for us to like start analyzing, right? Eventually.

23:31 - Matthew Kerns (12kernsmatthew@gmail.com)
Yeah.

23:31 - Chris Andrade
mean, I think we could get that through the pipeline of, of, of completing opportunities. Like, so, cause I got two sitting right here that I have to upload the audio file somewhere. You know what mean? Yeah. Like we can put out two customer portfolios with two different onboarding calls. Yeah.

23:56 - Matthew Kerns (12kernsmatthew@gmail.com)
Cause I mean, the process right now is documented. In my OS. So like, as soon as we get you set up with it, then you can run that same process, right? That's the beauty of SOPs. Right, exactly.

24:11 - Chris Andrade
Exactly. And then now I just alleviated a task off of yours and Mikael's plate, then now all you guys got to do is just analyze what you would have, what would have taken you 30 minutes, whatever it would have been. And now you get to just actually just go to work right away when you turn your computer on. You know what mean? Not having to build it, send it, create it, transcribe it. No, you get to have it done for you on your desk, ready to go. Like I can assist you guys there too along the intake process ultimately to help speed up the proposal turnaround, you know? Because Prince had three hours and like one day, I was like, oh son. mean, yeah, that's cool. If you say we can do that, then A. So I've We get to work, you know, and this is a huge step what we're doing on that. And again, now we're recording our screen to see, oh, damn, I'm already low again. So, yeah, what happened?

25:19 - Matthew Kerns (12kernsmatthew@gmail.com)
Did you do...

25:20 - Chris Andrade
No, I just put $5 in there. I was just thinking I wanted to see how fast it would run away. Okay. Well, what's , let me show you that, because now I'm kind of pissed. I actually put $25 in, and I don't, I'm so, I'm a little irritated because I guess I put it in the wrong... Let me see. No? Maybe this one? Hold on. So I bought... So I thought it was like I was buying okay let me just put $20 on this credit right so then I go into here and it's like no I need to put it towards my developer platform so I paid 30 bucks in this monthly spending limit when I should have put it in a whole a developer spending the no the developer one is like when we set up so when we set up automations or chatbots where it calls the API in the back end that's the developer balance so that's 20 to this I'd have to just keep so this is where the this is where that hundred dollar a month comes in well so So

27:00 - Matthew Kerns (12kernsmatthew@gmail.com)
This is something that me and Trent and Mikhail kind of discovered the other day because we were trying to set up a meeting processing automation that does this meeting processing step automatically so that nobody has to do it. Like you don't have to do it or anybody. But what we ran into, so what we discovered is that this developer console, there's like a separate developer side of things where the API gets called in the back end. Where you set up like a software, like a chat bot or an automation that calls Anthropic and that's its own charge thing and that doesn't pull from your Claude plan, like your Claude plan that's 20 bucks a month right now and the extra usage that you bought, that will just go to like when you use Claude code, when you use Claude, it's like the user side of things. So there's separation between user and developer side, if that makes sense.

28:00 - Chris Andrade
Yes, and that's where I'm trying to, so that's why when I asked, so I asked, when I first started signing up, this deal came up for, hold on, I need to let my dog out real quick. Give me one second, let me use the restroom. Give me, give me like a few, few sticks.

28:20 - Matthew Kerns (12kernsmatthew@gmail.com)
Sounds good.

28:56 - Chris Andrade
So that's why I bought the, I don't know. know. I don't know even what this is used for, and I don't know if this could even be used for anything that we need, so I don't know.

29:18 - Matthew Kerns (12kernsmatthew@gmail.com)
Yeah, you mentioned this a while ago, right?

29:21 - Chris Andrade
I just bought this, like, last month. Like a Black Friday deal or something? Yeah, because it was normally $1,000, and I got it for $300. And it has all, it's an agency startup kit.

29:36 - Matthew Kerns (12kernsmatthew@gmail.com)
Cool, sweet. Yeah, I mean, like, so this is all, like, marketing-related, so definitely.

29:43 - Chris Andrade
So there's nothing that we can use to ultimately help us with what we need right now to kind of host or get.

29:53 - Matthew Kerns (12kernsmatthew@gmail.com)
The QR code generator feature is something we can use for SNS. We can generate. Let's look through all the features and just be like, what can we use for certain stuff? Mikhail's gonna love the content generation stuff. You guys should have a meeting about that.

30:12 - Chris Andrade
That's in my AI tools? Yeah.

30:19 - Matthew Kerns (12kernsmatthew@gmail.com)
Interesting.

30:21 - Chris Andrade
Yeah, I haven't had a moment to really understand what I got here.

30:25 - Matthew Kerns (12kernsmatthew@gmail.com)
Yeah. Well, it's like, it's something you've already paid for. So any service that we're thinking, like, I know Mikhail's using Pomeli, which is a good one, but for image generation, it's like, if you've already paid for something, we can check it out and try and use it for their services. But like, what other services are there that are already paid for? In here? That's what we got to find out. Yeah. And we don't have to find out right now. Right. Yeah.

30:54 - Chris Andrade
And I think that's, I think we should probably do that between us for work. And think, Okay. And just an idea of what realistically are we already paying for, like what Trent did today, right? Bought us that feature.

31:10 - Matthew Kerns (12kernsmatthew@gmail.com)
Okay.

31:11 - Chris Andrade
And then understand how much are on the table do we already have and what is redundant or not?

31:19 - Matthew Kerns (12kernsmatthew@gmail.com)
Right. Yeah. Like, what do we need? What is available? What is already paid for? Because money coming in, in January, we should set aside a certain amount for tools. should have a budget for tools and we should pay attention to it and actually think about what we're paying for, right? Cost of daily cost of operations, right?

31:45 - Chris Andrade
What is our daily operating cost going to look like? know, so luckily we don't have a bunch of overhead. Yeah. All our, our overhead or what we're talking about, what we're looking at right now. So, and, and being able to, I guess. next time. Yeah. To do this, I'm going to have to add more... Oh, I need a... You said I need a copy, right? Not do that.

32:12 - Matthew Kerns (12kernsmatthew@gmail.com)
Well, the first problem is not that. The first problem is console.anthropic settings billing. So...

32:22 - Chris Andrade
I got to add more funds, like the same thing, what we had earlier, pretty much. So it's going to... Oh, wait, Fireflies is asking... Oh, wait. Credit balance. Oh, so... Yeah, what is it? It's in the meeting.

32:43 - Matthew Kerns (12kernsmatthew@gmail.com)
Okay.

32:44 - Chris Andrade
So I wanted to set up the integration for Fireflies, go to here, but then it said, hey, your credit balance is too low. So we got to add... We got to add more funds. And it looks like you can...

32:59 - Matthew Kerns (12kernsmatthew@gmail.com)
It said... As you can just do control click, but I don't know if I just didn't know.

33:04 - Chris Andrade
Yeah. So I used, I've already used this. This is what it costs me to finish out my OS built. Oh, okay.

33:15 - Matthew Kerns (12kernsmatthew@gmail.com)
Okay. So, okay. So there is a developer one that's separate, but it's not this. It looks like this is anthropic. Then there's a separate like developer one that we talked about earlier.

33:30 - Chris Andrade
So what should I do?

33:33 - Matthew Kerns (12kernsmatthew@gmail.com)
So I think, I mean, like, well, we got to figure out like, okay, is it worth it to go to the next tier up? Or should we just keep paying for more extra usage credits? We, we stayed on Opus. So what we could do is add like five more And then switch the model to Sonnet and see how long that lasts. That might be a good next step. Okay, let's try that.

34:09 - Chris Andrade
So then let's just do 10.

34:23 - Matthew Kerns (12kernsmatthew@gmail.com)
And I don't know like, if you upgrade to the next tier, I don't think, like, what it does is when you're paying $20, then if you go to the $100 tier, it will only charge you $80 for the money. That's what I figured.

34:42 - Chris Andrade
Like, I'm sure it would, like, my next month payment would get built of that. Okay, so now I got $10.78, and now I'm- I don't know if you can do the same for this extra usage.

34:59 - Matthew Kerns (12kernsmatthew@gmail.com)
Or not. if do that. It because I haven't tried that yet. You know what I mean?

35:04 - Chris Andrade
Say that one more time.

35:06 - Matthew Kerns (12kernsmatthew@gmail.com)
So like, I don't know if it will charge you. Like if you upgrade to the hundred right now, I don't know if it will charge it might just I know for sure it will. It will charge you. Right, right, right, right. It'll charge you 65 from this, right? Yeah. Oh, no, it probably won't because it's two different.

35:30 - Chris Andrade
Yeah, they probably won't. But we should we change it from Opus to the other one right now?

35:36 - Matthew Kerns (12kernsmatthew@gmail.com)
Yeah, definitely. How do we do that? So yeah, do slash model. Oh, that's right. Yep. And then default recommended. Yep. And then just tell it continue. So, yeah, this should last a lot longer.

36:09 - Chris Andrade
We were in Opus because it was having to, can we refresh why we switched again?

36:17 - Matthew Kerns (12kernsmatthew@gmail.com)
So Opus, we did Opus so that we could do the, like, there was the whole structure of the OS. Oh, that's right, yes. Yeah, and then there's a whole new one that was built out. So it's like this very complex thing to merge them, right? So, but what we should have done is immediately once that merging happened, we could have switched back. But we also had to do the implementation plan to build out the original OS. So, like, I think that's good to use Opus for that. Right.

36:49 - Chris Andrade
And that's why, so for $5, that's not bad. And now, so all the hard stuff is built. Now we're just making simple API calls. So will I need to pay for every transcript I push through with Claude like when you use Claude code CLI?

37:31 - Matthew Kerns (12kernsmatthew@gmail.com)
No, so okay, so nice thing I just realized is we probably didn't have to pay this 10 bucks because it just passed 1pm. Or wait, no, actually, it's 2pm your time, right? So that means we, we did burn through the limit. What the way that Claude does it is every five hours, there's a you have a certain amount. So you can burn through your limit. And then at the next five hours, you get more credits. . Oh, gotcha. Yeah, which is really cool.

38:02 - Chris Andrade
I mean, yeah, so it looks like based on ASU. So it looks like, what do we got here? Oh, so it built the folder structure.

38:16 - Matthew Kerns (12kernsmatthew@gmail.com)
Yeah, so this is the commit message. So this is just saying, this is giving you a summary, and it's also committing it locally to Git. So it's like saying like, all these changes did this, let's package that up, put it in one commit. So API integration with Python, sync script, processing workflows and templates, action items, tracking system, action items by client, by type, raw transcript, processes, template workflows, integrations, fireflies. I don't see summaries, I guess by client. do we do? Uh... ... ... ... Yeah, pulls full transcripts and summaries, auto-extracts transcript summaries, action items, metadata. I think it's fine. It'll store the summary by client. I don't know how it's going to do by client and by type, but let's just see how it does it. Maybe it does it better than what I was thinking. Usage, configure Firefly's API key. So that's something that you got to do. So can you do control and then click on where you see the path where it says integration slash Firefly slash .env Yes.

39:34 - Chris Andrade
Wait. Yes. This top one. Number one. Yeah.

39:38 - Matthew Kerns (12kernsmatthew@gmail.com)
So hold down the control on control button on your keyboard and then mouse over that path. Like you don't have to highlight it or anything. Just Oh, right here. Like this.

39:49 - Chris Andrade
Yeah. And then not the AP.

39:51 - Matthew Kerns (12kernsmatthew@gmail.com)
Actually, yeah, you can try and click on that one. See what happens. No. Okay. Go to the path on the right where it says the slash. Yeah. Integration slash Firefly. Oh, got it. Okay. Click on that. Okay. Yeah, there you go. Now it opened it up. You see up top? Okay. So now where it says your API key here, just paste your API key from Fireflies. Where do I paste it? Right at the bottom. Oh, number 12? No, like, you see number 11. here. I see. Got it.

40:44 - Chris Andrade
Leave the equals? Yes, definitely.

40:48 - Matthew Kerns (12kernsmatthew@gmail.com)
And then save, do control S to save this file now. That's important.

40:55 - Chris Andrade
So I hit just control save and it doesn't show. Yeah. It's been saved. just saves it.

41:02 - Matthew Kerns (12kernsmatthew@gmail.com)
So yeah, so type or hit enter right now. So you see that at the top, how that dot appeared on the tab. That tells you it's not saved. So yeah, so now if you hit save, that dot goes away. Got it.

41:19 - Chris Andrade
Awesome. Thank you for that.

41:21 - Matthew Kerns (12kernsmatthew@gmail.com)
Cool. Awesome. So now what you can do what I would recommend is just instead of saying yeah, actually, you can say yes to proceed. So yeah, yeah. So yes. And then we're going to type. After that, I uploaded my Fireflies API key just now. Oh . It erased it. It erased it.

42:00 - Chris Andrade
Yeah, it was like, it checked.

42:04 - Matthew Kerns (12kernsmatthew@gmail.com)
Well, so tell it. Wait, what is it doing? Go to Fireflies, echo, key equals this to env. Oh, I see it's doing Yeah, just tell it yes to proceed. It's fine. It's doing the right thing, I think. So it already you don't even have to tell it I've uploaded my key it already knows. Oh, cool.

42:31 - Chris Andrade
Yeah. Yes.

42:47 - Matthew Kerns (12kernsmatthew@gmail.com)
So that's good what it did. Before it pushed to GitHub, it removed it from it removed the API key. So you don't want to push credentials to. To GitHub, because if somehow that repository gets public, or people or someone just gets access to that repository, they can look through the whole history of the Git repository. And they can pull API, they can just search the history for API keys and be like, Oh, now I have access to your account, especially with Claude. It's like super, super easy. So that's crazy.

43:25 - Chris Andrade
So because it asked you, it shows that it's like, has this, like a security invention? Or like, what is it? What's your thought there? Like, it's like, proactively taking the security into mind in an account?

43:40 - Matthew Kerns (12kernsmatthew@gmail.com)
Yeah, basically, it, it prevented you from uploading the API key to GitHub, which was really cool. It won't always do that, by the way, it'll sometimes it'll mess up. So we got to be careful, but Got it.

43:55 - Chris Andrade
I'll note that if I'm ever having to do that. Yeah. Yeah.

43:59 - Matthew Kerns (12kernsmatthew@gmail.com)
You Yeah, another thing we can do, like if we create, say we create for Potter Mechanics, we create a repository for them, we can scrub the whole history for API keys and just make sure that it's not there before we give it to them. So it looks like it's done.

44:20 - Chris Andrade
says push to GitHub and ready to start syncing your meetings. Yeah, tell it like...

44:29 - Matthew Kerns (12kernsmatthew@gmail.com)
It says test the Firefox sync script now?

44:32 - Chris Andrade
Yeah, let's do it.

44:36 - Matthew Kerns (12kernsmatthew@gmail.com)
It might not work the first time, but maybe. We'll see.

44:40 - Chris Andrade
Let's do it right now. Again, this is... Proceed. This is a tutorial for future clients that have Firefox. Firefox... Just don't ask again for all this. Yeah, you got it. See, like, we'll never have to do this again to anybody, bro. Maybe one more time, but maybe more professional, like a blue-collar setup, you know? Or, like, when we're actually doing it for a client in live, you know what mean? Yeah.

45:33 - Matthew Kerns (12kernsmatthew@gmail.com)
Like, once we have these, once we have the videos built out and, like, professionally kind of made, then we can just hand it to them as, like, here's your training videos. Right. You let us know if you have questions now.

45:48 - Chris Andrade
So it says bash command where this Python was not found path check for Python installation.

45:55 - Matthew Kerns (12kernsmatthew@gmail.com)
So this kind of thing happens a lot where it'll just run into error. And I always just like kind of click through and I just say yes and don't ask several times so that it can just figure it out and work and it'll learn things as it goes. So you won't have to always run into this like the more you use it, the more it'll just kind of know. But some things, sometimes if you notice the same issue happening a bunch of times, you can tell your ClaudeMD to, you can tell it like, hey, we keep running into this issue, let's update our agent instructions, which is the ClaudeMD file, to just know the right thing to do, so.

46:46 - Chris Andrade
And so yeah, it looks like it's found the path at the Python setup for the integration and then get push. So I would say, I would say don't.

47:00 - Matthew Kerns (12kernsmatthew@gmail.com)
Get push, like go down to type here and tell it to stop pushing everything like we don't need to push every change. Let's just keep working for a bit. So say what? We don't need to push every change for now. Yeah, because it right now, it's in a loop of it wants to push every single change because you've accepted get push a few times. So it thinks like, oh, I need to push often. Oh, I see.

47:39 - Chris Andrade
So then download option for Python recommended. Got it. No need to push test fireflies quick install Python important add Python to path your install.

47:55 - Matthew Kerns (12kernsmatthew@gmail.com)
So yeah, it's asking you to install Python, but we're going to ask it like Can you help? Can you install Python, please? And the please, I think, is a good thing to add. Might, might cooperate a little better, if we're polite.

48:16 - Chris Andrade
Yeah, so that I forget somebody who actually like, we actually like tested that or not tested it like, you know, it might put me in a list down the road when it takes over and like, this guy was polite to me, even though I was not just a thing.

48:31 - Matthew Kerns (12kernsmatthew@gmail.com)
Yeah, you don't got to wait for it to take over. It'll be more pleasant to use right now.

48:37 - Chris Andrade
So it's asking to download the Python installer. We're going to go ahead and say yes. Yeah, sir. Install Python silent. I'll a So if I wanted to install this bot on my Mac computer, how How complicated is that process? it like another pretty much a full iteration of this? Pretty much.

49:37 - Matthew Kerns (12kernsmatthew@gmail.com)
Like you're gonna need to install, make sure you have Node.js installed, Python installed, all this basic stuff. You're have to redo. What does that say?

49:49 - Chris Andrade
Oh, I was just asking for something.

49:56 - Matthew Kerns (12kernsmatthew@gmail.com)
Yeah, that's fine. Just hit close and then let's see what Claude thinks now it's imagining so I thought by Python installation yep do it okay I found it so that's good that means that the path is correct I believe so now hit proceed so it's trying to install request package using pip so pip is like an installer all right oh pip right here yeah run so and like yeah so hit yes to proceed um so now it's using Python to run the script that it made for the first time so often there's like errors when it Like, it'll create a script, and it'll do a really good job, but then it'll have, it might not get everything just right, so. There it is.

51:09 - Chris Andrade
It fixed the script.

51:12 - Matthew Kerns (12kernsmatthew@gmail.com)
That's what I'm approving. Yep. Now it fixed it, and it's going to run it again, so it might be another error again, but it might just work, so we'll see what happens. Dude, this is, like, this is wild.

51:25 - Chris Andrade
Like, this is.

51:27 - Matthew Kerns (12kernsmatthew@gmail.com)
Yeah. Yep. It's crazy, dude. So now it looks like it worked, so it's good at creating the thing, it doesn't get exactly right, and then it's good at fixing it up, so. First small, for little things, like, a little script, it can do, like, there's times where it's too complicated of a task, and it'll just be stuck in a loop. Or it'll take longer than, or a developer overseeing it to get. to the final result right which is why developers still have a position and like a role right um so it's still west still testing the scripts to fix it yeah i would say yes and don't ask again so that it in case it needs to do that again it'll just hopefully do it and it'll fix it and then do it and then you know i gotta go grab some water real quick i'll be right back okay good yep i do too go get some and i'm gonna take a leak

55:11 - Chris Andrade
I came back the same time, and I did not do the dishes, so if you want to proceed, run with debug mode?

55:30 - Matthew Kerns (12kernsmatthew@gmail.com)
Yeah, I mean, yeah, OD, yes, and don't ask again. What's debug mode? It had a, I think it's part of the script that it's making. It was like an option in the script to run with debug, so it'll just print more logs. So one thing I was thinking just now is like, you, I like, I like how you just got started on like, okay, let's build This thing, this integration, this is, there's a chance that right now we're on a path that could take like a couple hours. And ideally, maybe I should like, think about the integration and design it so it doesn't, because the coding agent will tell you it can do it. And it will get caught in the loop if it's too complicated of a task. It might, it might be fine. It might work. So I don't know that.

56:29 - Chris Andrade
Fireflies is synced, working perfectly. All right. yeah. So it's like files created, next step, process meetings using workflow, updated tracking, add meetings. Want me to commit these changes now? Or would you like to test syncing?

56:52 - Matthew Kerns (12kernsmatthew@gmail.com)
Ask it to, ask it to pull all your meetings from this last week and tell me about them. See if we can do that.

57:05 - Chris Andrade
I'm gonna say pull my meetings from last week or like yeah this week maybe you said you're meeting I only had two last week so I'm curious to see what it's gonna pull up I'm sorry bro I keep like cooking and eating on our calls and stuff but don't be sorry bro you live it you living you're a high metabolism dude I really am son of a I'm trying to I've been trying to gain weight for 30 years dude and I'm

58:00 - Matthew Kerns (12kernsmatthew@gmail.com)
I'm like, I have a goal now, I'm trying to get to 170 by April, and I've been at 158 for like a year, so I don't know, we're going to try and make this happen, but I got to eat.

58:11 - Chris Andrade
So it's saying it wants, what's CD? CD is like change directory. It's wanting to change directory from its operations integration Fireflies.

58:30 - Matthew Kerns (12kernsmatthew@gmail.com)
So what this is doing is it's changing, so it's your cloud is in, it starts out at the top level of like cloud code OS, and it needs, the script lives inside that O2 operations, integrations, Fireflies path. So it's changing into that directory and then it's running. The script, and then it's running it with the arguments sync, it's running it, the script is called syncmeetings.py, so it's running that script with arguments days seven. So it's asking you, should I run the script with this argument? And this is the argument. Yeah, the days, days seven is the argument. Syncmeetings.py is the script file.

59:34 - Chris Andrade
Oh.

59:36 - Matthew Kerns (12kernsmatthew@gmail.com)
Yeah, and then python.exe is the thing that runs it. It's like, that's Python. Ah.

59:45 - Chris Andrade
That's the Python executable.

59:48 - Matthew Kerns (12kernsmatthew@gmail.com)
Okay.

59:50 - Chris Andrade
And so, what is, why is it finding a similar command here?

59:55 - Matthew Kerns (12kernsmatthew@gmail.com)
It's saying yes or yes and don't ask again for. Okay. Similar commands. Oh, cool. Okay, got it. I see.

1:00:06 - Chris Andrade
So this is what you want to see, in other words.

1:00:09 - Matthew Kerns (12kernsmatthew@gmail.com)
Yeah, like, I would, like, if I know, so I know it's going to try and run a bunch of times. Like, every time I want to use this integration, like, try and pull meeting information, it's going to run a similar command. So I would say yes, and don't ask me again, because I know that I just want it to run it. don't want to have it ask me. Yeah. Some things that you might want it to ask you, like, there might be a script that you make that's like, you know, reorganize my stuff or clean up files or delete things. And like, then you want it to ask you. But yeah, definitely not everything. So, and sometimes it doesn't, it doesn't always, it doesn't always work with the similar commands thing. So you have to tell it, yes. doesn't go. A bunch of times still.

1:01:01 - Chris Andrade
I'm curious, why did it go from, why does it want to do it now, 14 days?

1:01:09 - Matthew Kerns (12kernsmatthew@gmail.com)
You can do, okay, you can do control O. So you see where it said it ran the first one and then it said control O to expand. So now this gives you like the output. So it says synced one meeting location in this raw transcript. So, but it, so then you can see what it was thinking too.

1:01:36 - Chris Andrade
Oh, so it gives me information about what, can you have fun?

1:01:41 - Matthew Kerns (12kernsmatthew@gmail.com)
Yup.

1:01:44 - Chris Andrade
That's awesome. I'm so proud. I'm not going to kick my butt. Cause I need new dishes. Gotta do those dishes, man.

1:01:55 - Matthew Kerns (12kernsmatthew@gmail.com)
Yeah.

1:01:57 - Chris Andrade
So. So, yeah.

1:01:59 - Matthew Kerns (12kernsmatthew@gmail.com)
It's. You see where it says thinking? And it tells you what it was thinking. it's like... it. Yeah. That's cool.

1:02:08 - Chris Andrade
So then I could just... I didn't want to say yes then, right?

1:02:12 - Matthew Kerns (12kernsmatthew@gmail.com)
So what does it say there? It says only one meeting in the last seven days. Let me check if there are more meetings by extending the meeting time. 14 days.

1:02:22 - Chris Andrade
I think, yeah, 14 days would be good.

1:02:24 - Matthew Kerns (12kernsmatthew@gmail.com)
Okay, cool. Yeah.

1:02:25 - Chris Andrade
So then how do I get back?

1:02:28 - Matthew Kerns (12kernsmatthew@gmail.com)
Control O again. Okay. Control O.

1:02:33 - Chris Andrade
And then... Let's see. Hold on. Babe, I'm sorry. I ate into the dishes. Babe, I'll let you enjoy your food for a second. Let me go knock this out. Do you want to just stay on or I don't know. I'll call you. Yeah, I'll just stay on, but just take your time.

1:03:05 - Matthew Kerns (12kernsmatthew@gmail.com)
Whatever time you need, just do it, and we'll always reconvene later.

1:03:10 - Chris Andrade
I'll keep coming back and making sure that this is staying updated. can put this so I can see it from the kitchen. So let me just knock this out. be right back. Sounds good, bro.

1:03:35 - Matthew Kerns (12kernsmatthew@gmail.com)
Looks like it's working. Thank you. Thank you. Okay. Thank you. you. you.

1:07:19 - Chris Andrade
Oh, man. She's running still. I'm still doing some dishes, but I just unloaded. I got to scan the desk up.

1:07:29 - Matthew Kerns (12kernsmatthew@gmail.com)
Yeah, it's working, dude.

1:07:32 - Chris Andrade
Hold on. Let me finish. I'll be right back.

1:07:57 - Matthew Kerns (12kernsmatthew@gmail.com)
I'll be right back. I'll be right back.

1:12:27 - Chris Andrade
You still rolling on?

1:12:33 - Matthew Kerns (12kernsmatthew@gmail.com)
Yeah. Looks like it's still going.

1:12:38 - Chris Andrade
So is it because it's the first time, so it's building it all out, and next time it won't take so much?

1:12:48 - Matthew Kerns (12kernsmatthew@gmail.com)
Well, I think it's got a lot of meetings to process. Now what it's doing is it's writing Brandon Heck overview. Thank you. Thank you. Thank Oh, .

1:13:03 - Chris Andrade
So it's going through all of, bro, what the hell? That's crazy. Oh, my. Oh, my.

1:13:16 - Matthew Kerns (12kernsmatthew@gmail.com)
Retail client, that's the one.

1:13:18 - Chris Andrade
Oh, that's it. Oh, my gosh, dude, this is sick. This is, this is what I was, Matt, bro, what my concern about this morning is seeming to kind of go away now. Now I'm paint the picture. Now it's starting to make sense. I was like getting a little concerned. And I was like, I'm not, I don't feel so lost anymore. So this is awesome.

1:13:48 - Matthew Kerns (12kernsmatthew@gmail.com)
Sweet. Yeah. I'm glad we're making good progress. Yeah.

1:14:01 - Chris Andrade
Bless you. Speak to that. I'll be right back. I'll be right back. Thank So I can finish.

1:23:10 - Matthew Kerns (12kernsmatthew@gmail.com)
Yeah, should we see what it says on the top?

1:23:19 - Chris Andrade
All five meeting. Okay. Okay. All right. Interesting. So I'm wondering what these two are. Okay. So I can reference the summary from my... What it just imported. Like, I can have a conversation about the information I need to get out of it through this interface, right? Commit. Or what does it mean, like, commit these media files to get. Oh, so it's trying to push it to get.

1:24:24 - Matthew Kerns (12kernsmatthew@gmail.com)
Okay. does it say commit them? Oh, yeah. Yeah, I would. I would do that. Yeah. Okay. Push. Because every time you're done working on your computer, if you want to access from your phone, you got to commit and then also push. Remember to push.

1:24:40 - Chris Andrade
Okay, so now it's pushing. No.

1:24:45 - Matthew Kerns (12kernsmatthew@gmail.com)
Now it's just committing. Oh, okay. Okay. So I can show you what that means. But it's basically like, just your local changes haven't been packaged up into a commit. Once they're in a commit, then they can be They They can't be pushed without being committed to the two-step process.

1:25:06 - Chris Andrade
Yeah. Okay.

1:25:10 - Matthew Kerns (12kernsmatthew@gmail.com)
This whole thing is a commit message. So it's to keep track of all the changes that were made at one time. So you can look back and be like, oh, that set of changes does this and this and this. Awesome. Yep. So then once you commit it, then you can tell it to push or it might try to do that anyway. But you just told it to not push. So you might have to tell it to push.

1:25:45 - Chris Andrade
Yeah. So you want me to proceed? Yep.

1:25:53 - Matthew Kerns (12kernsmatthew@gmail.com)
So now like I whenever it does something like this, I like to look at the organization of it and see. see. There's If that's, if it's good, so, and also just know where it put that stuff. So you can do like control click and look through and look at where it said over there. Like, yeah, I go back up to where all files were now saved to at the bottom or just active items. Yeah. Control control. Yep. And then, so this is, this is like the current list of active items. That it came up with. So this is one way to do it. don't like, you could always say like, you know, I want to organize a different way or whatever. But for now, I think this works.

1:26:41 - Chris Andrade
100%. Okay, so if I ever wanted to enhance what I've seen. Okay, I won't even go. I get it. I get it. I get it. I'm sorry to understand. Okay.

1:26:58 - Matthew Kerns (12kernsmatthew@gmail.com)
Yeah. You can do it however you want. This is the structure of ultimately the results. Yeah. Like these are the action items that it pulled into action items. I think if you open up on the left, you can see where this file is highlighted. And then if you go down to buy client, we can see if it did something there. Nope. So what does that read me? Okay. So the process didn't do this. It didn't organize by client yet. Not yet. You could tell it to do that and it would do it. would follow this read me and it would do it. Then by type, can you open that one and see if it did anything there?

1:27:42 - Chris Andrade
How do you know it did something or not? There would be more files.

1:27:46 - Matthew Kerns (12kernsmatthew@gmail.com)
So you see on the right where it says structure at the top, like you scroll up a little bit. It says structure and then it has by client, client name, read me. So this is what What it will look like, like it'll have under the by client folder that only has the readme right now on the left, you can see in the file explorer. It only has the readme, right? So like the structure that it's the readme is telling is instructing itself to do is like, okay, let's put client name and then we'll put meeting topic relationship status and the readme with a client overview. So that's the structure it's currently planning, but you can make it however you want. You just need to tell cloud code and then it'll update the right files and all that good stuff. So yeah, so I see what I'm starting to understand.

1:28:44 - Chris Andrade
So yeah, by type, same thing says readme. So it doesn't look like nothing in here then, right?

1:28:49 - Matthew Kerns (12kernsmatthew@gmail.com)
Yeah, so it set up the structure, but it didn't, when it ran through everything, it didn't, the process that it's following didn't quite update all that. Those other files, but it did, looks like it uploaded the raw transcripts here. Yeah. And I don't know if it, what's that process folder inside there? What does that have? Okay.

1:29:16 - Chris Andrade
Decisions, overview, roadmaps. Yup.

1:29:21 - Matthew Kerns (12kernsmatthew@gmail.com)
And then there's that summary.md. Is that, what is that if you open that one up? Okay, so that's a summary of that meeting. So you have a summary. I don't know if this is the Fireflies summary, because I don't know if we integrated with the Fireflies with the correct API.
ACTION ITEM: Add Fireflies Summaries API to sync script; integrate into my OS; then Chris pulls - WATCH: https://fathom.video/share/FAR87xKdceD-xoqqchGFvu-xnAUJ5qM2?timestamp=5378.9999 I know it integrated with the transcripts API. So Claude might have pulled the transcript and then done its own summary thing. So to upgrade the summaries that you get out of Fireflies, you're going to want to integrate directly with the Summaries API now.

1:29:58 - Chris Andrade
Interesting.

1:30:00 - Matthew Kerns (12kernsmatthew@gmail.com)
Yeah, but I can work on that, too, and then I can get it going in my OS, and then you can just pull it. No, I can't see.

1:30:10 - Chris Andrade
I don't want to over-round them. Like, this is all a work in progress, but this is a hell of a starter. Yeah, yeah.

1:30:20 - Matthew Kerns (12kernsmatthew@gmail.com)
Like, I would say, I would say just, I think it's burned all these eggs.

1:30:31 - Chris Andrade
Hey, I think this would be a perfect time to, oh wait, install, install, and do I need to finish anything up over here real quick?

1:30:42 - Matthew Kerns (12kernsmatthew@gmail.com)
Yeah, do make sure it's pushed. So, at the end, just tell us.

1:30:48 - Chris Andrade
Processing in actual intelligence. Push to GitHub. So, we want to push now, right? Yep. Does this take a minute or Should this be fast too?

1:31:01 - Matthew Kerns (12kernsmatthew@gmail.com)
That'll be fast. Oops. So then once it's pushed, then you can, you can, on your phone, when you start a new session, then you can ask it stuff about the transcripts get pushed to.

1:31:26 - Chris Andrade
And once you start understanding how this is going to play out.

1:31:34 - Matthew Kerns (12kernsmatthew@gmail.com)
Yep. You just integrate with Fireflies, dude. This is something that we've been talking about doing. Like, we've been like, oh, should we integrate with Fathom? Like, yeah, we should do it, but we're, we're going to prioritize it. Blah, blah, blah. You're just like, I just want to do it. I'm just gonna do this right now. And you just did it.

1:31:51 - Chris Andrade
Well, cause he, cause I, it's the next step of, by flow, right? Cause now if I can now. I just continuously keep plugging fireflies and just overload this with all my thoughts, all my everything, and just like, if we have an overload of opportunity, now we have our own opportunity matrix that we can run off of. Yeah.

1:32:23 - Matthew Kerns (12kernsmatthew@gmail.com)
Not other companies, our own.

1:32:26 - Chris Andrade
That's kind of my thought here. Yeah, bro.

1:32:30 - Matthew Kerns (12kernsmatthew@gmail.com)
I love that. Oh, what?

1:32:32 - Chris Andrade
Drafting Tyler follow-up email? Yo, that's crazy. What? No, sirree. You stuck. You stuck. It's not working for a lot. That is crazy. Yeah. Yeah. Yeah. You slow your roll, mister. See?

1:32:51 - Matthew Kerns (12kernsmatthew@gmail.com)
That's crazy, though.

1:32:54 - Chris Andrade
So that's a kind of a really big win. I think this would probably be a really good place to stop the- Because we just kind of made another configuration. And let me get some stuff wrapped up in the home real quick. And then Toby with Maples Apothecary should be calling in for that meeting. I just don't know when he's on his way home. They're picking out a bunch of plants right now from California. Oh, shoot.

1:33:29 - Matthew Kerns (12kernsmatthew@gmail.com)
They're in San Diego, actually. Okay, all the to California. They ain't as far.

1:33:33 - Chris Andrade
Yeah, they're even... So they're really... So, dude, wait. I can't wait. Dude, wait until you guys hear the story of Mr. Maples and I. It's a pretty cool one. So I don't want to spoil anything away.

1:33:47 - Matthew Kerns (12kernsmatthew@gmail.com)
But yeah, so... San Diego is like an hour and a half or two hours from me. So they own a store in Yuma.

1:33:56 - Chris Andrade
You know where that's at? Yuma?

1:33:58 - Matthew Kerns (12kernsmatthew@gmail.com)
Like the movie? 310... Yeah, yeah, yeah. I don't know where that is. Is it Arizona?

1:34:05 - Chris Andrade
It's right on the border, Cali and Arizona, the tippity-bottom, the tippity-dipp. Okay, cool. Yeah, so they own, wait till you hear, man. This is one of those, I can't wait to tell you guys. So yeah, we'll end here on this and then yeah, let's log this up as our, the integration for Mr.
ACTION ITEM: Post next steps in Slack to Chris - WATCH: https://fathom.video/share/FAR87xKdceD-xoqqchGFvu-xnAUJ5qM2?timestamp=5668.9999 Fireflies. And then we'll be able to expand on that and yeah, we'll figure it out.

1:34:39 - Matthew Kerns (12kernsmatthew@gmail.com)
I got some next steps for us, so I'll put it somewhere. I'll put it maybe in the chat with you in Slack and then we can go from there.

1:34:48 - Chris Andrade
And if you, if you have, if you want to work them out, I have no problem. Let me just get a couple of things wrapped up and I'll get right back on. Okay, whatever works.
ACTION ITEM: Run Maples Apothecary discovery call w/ 5-question framework; introduce Matthew & Mikael - WATCH: https://fathom.video/share/FAR87xKdceD-xoqqchGFvu-xnAUJ5qM2?timestamp=5694.9999

1:34:56 - Matthew Kerns (12kernsmatthew@gmail.com)
Yeah, know you got that meeting coming up too. So maybe if you recharge for that. For the meeting with, oh, for Toby.

1:35:05 - Chris Andrade
Yes. Yeah. He's more, that's more like a, I've got general kind of, like a catch up conversation too. But I'm going to integrate the five question framework as well. And I would love to introduce you and Mikael. So hopefully, Trent, I mean, depending on what time he is, I'm going to be on the road back because he said he was going to call me when they're going to go get dinner. And then that will give me an hour heads up. So we're still now at three. So we're looking at 430. If you don't hear from my four, that's a 536 conversation. So that'll be perfect. Okay, cool.

1:35:45 - Matthew Kerns (12kernsmatthew@gmail.com)
Well, this stuff that I have next is just discovery process related. So anytime we want to do that, we can do it. Yeah. Okay.

1:35:54 - Chris Andrade
Sounds good. I will ping you here in a minute. Sounds good, bro.

1:35:58 - Matthew Kerns (12kernsmatthew@gmail.com)
All right. High five. Have fun, talk soon. Bye.
