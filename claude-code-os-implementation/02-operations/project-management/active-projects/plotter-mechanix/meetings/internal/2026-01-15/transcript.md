# Internal Development Meeting - January 15, 2026

**Attendees:** Matt, Trent
**Project:** Plotter Mechanix - Phase 1

---

@Matthew Kerns [0:10]: I'm ready Sick of not making progress on this, so I'm, I'm ready, But I did, I do think it was really important that I did the calendar stuff earlier and The thing that you shared was super helpful. So I walked through all that, gave it a bunch of context, and got my calendar way more organized, so that, that helps. But yeah, so.

@Trent [0:33]: Yeah, it took me a while to go walk through that too, to just like. Look at what I had in my calendar and really think about what I was Putting in my calendar and how it was gonna work for me, and I moved to like my gym time and I moved some other things around to

@Trent [0:50]: Sort of Maximize this, this idea anyway, or at least make an attempt to.

@Matthew Kerns [0:56]: Yeah, and I think it might for a little while, I just ended up manually moving stuff, like reclaim I think is going to be awesome, and there's, it's good that you can, I can put parameters there cause it gets it mostly right, but then I definitely need to manually move some stuff for now, which is fine, but

@Trent [1:13]: Well, the stuff that is in your calendar that it was not originating from Reclaim, stays there. It works around it.

@Matthew Kerns [1:23]: Yeah Yeah.

@Trent [1:25]: So.

@Matthew Kerns [1:25]: So I had to do a bunch of edits in my Google Calendar for that, but it's, it's a lot more cleaned up now, so I think it was massive progress today. It's just going to be refinements now. so, yeah, and that's, that's gonna like

@Trent [1:37]: Yeah

@Matthew Kerns [1:41]: Be super impactful over the next few weeks. Obviously, as long as they stick to the calendar, but that's the goal, so, Yeah.

@Trent [1:51]: Got it Nice, nice

@Matthew Kerns [1:55]: So right now I have a focus block from 4 to 7. I'm gonna see if I can go longer. Or But I do need, there is like a meal prep and learning time. For an hour after that. So that'll be a good break, and then maybe I'll do another one, depending how things go, but

@Matthew Kerns [2:16]: Yeah, I'm just gonna focus on this block for now.

@Trent [2:18]: OK, I'm going to share my screen if I can. Let's see.

@Matthew Kerns [2:25]: OK.

@Trent [2:28]: Yeah Let's see Screen 123, which one, this one here. Yeah, that's it OK So what I was trying to do is fix a bug or a couple of bugs here that it had so far.

@Trent [2:51]: Just starting with the daily summary. The daily summary, all it is is it just, it sends a notification to the plotter mechanics channel, right here. Does this

@Matthew Kerns [3:02]: OK Nice.

@Trent [3:04]: So there have been 20 total events, 20 transcripts, and 12 unique callers.

@Matthew Kerns [3:10]: OK.

@Trent [3:10]: So. It just does that at 6 p.m. I think Eastern time. So, I just thought that was kind of cool to just see an update every so often. So I was like, OK, let's just try that out. But one of those things that

@Matthew Kerns [3:21]: Yeah

@Trent [3:24]: What triggered me to do that really was I was talking to Claude and I'm like, hey, if there's an error I'd like to know. So there's an error handling in here, and one of the things it does is it posts to Slack if there's an error.

@Matthew Kerns [3:39]: OK

@Trent [3:40]: But one of the problems I had was this was actually, there was an error occurring in here. So,

@Matthew Kerns [3:48]: Yeah

@Trent [3:49]: It kept having an error, for this because it was having a data type mismatch. It was saying phone number expects a number, but we got unknown, unknown as text that can't put text in a a number field. So, I had to fix that bug, and hopefully that works now. I can maybe will let me, I think it'll let me cue it, so let me see here.

@Trent [4:13]: To do like, I think you pin it or something, yeah, pin this data, pin data pin will always

@Matthew Kerns [4:20]: You can copy the Jason.

@Trent [4:23]: Hold on, it has 10 will always output current data instead of executing. So if I debug an editor, it pinned it for me. So now if I do this There it worked. So now if we were to go and look at the

@Trent [4:42]: You see what I did there So if you go to executions at the top.

@Matthew Kerns [4:48]: Mhm

@Trent [4:48]: Do all your executions on the left Right? You can see the current state or the state at the time that the error occurred, right, or with the execution occurred?

@Matthew Kerns [4:56]: Right. Yeah, yeah, of course.

@Trent [4:57]: And then And if you pick it Right? And then you just hit debug and editor, it'll take the data that came in and it'll pin it. So you hit debug and editor And you can see

@Matthew Kerns [5:08]: Yeah.

@Trent [5:09]: I'll go back

@Matthew Kerns [5:10]: So debug and editor is what did the pinning.

@Trent [5:13]: Yeah, it pinned it right here. See the purple? With a little

@Matthew Kerns [5:16]: Yeah.

@Trent [5:17]: Little pin on it

@Matthew Kerns [5:18]: Mhm.

@Trent [5:19]: You can unpin it by like just unpinning that, you just check it, and it

@Matthew Kerns [5:24]: Got it. OK, so I didn't know that you can do that. So that's like for a failed execution, you can just

@Trent [5:24]: Updates. Not just fatal

@Matthew Kerns [5:29]: Debug it

@Trent [5:31]: Any execution, so you can just test it and debug it, right?

@Matthew Kerns [5:34]: Yeah.

@Trent [5:36]: Mhm

@Matthew Kerns [5:36]: OK, but from the execution, you hit debug an editor and then it'll bring it to the editor, the data that came in.

@Trent [5:41]: Yep, yep, yep, the, yeah, the workflow is like you wanna go view it, here's the problem. I see a problem. You can see the, the The angled stripes, right? And then that means you're in execution mode, not in edit mode, so you can just click debug and editor based on whatever you pick, it'll pin that data. You can currently go in here and see the data, right? This is what happened.

@Matthew Kerns [6:03]: Yep

@Trent [6:07]: But at the end of the day, what I really want to do is I want to fix the problem. So if I want to fix the problem, I can go into the editor, and I already had Claude Coat fix the problem, but I wanted to test a previously

@Matthew Kerns [6:08]: Mhm

@Trent [6:20]: Occurred execution, right? So I wanted to use the same data that caused an error before. So now if we go to here at the plotter, yeah, look, quote a job or error, validation of table request unknown matches, so it's spitting out a

@Matthew Kerns [6:27]: Yeah.

@Trent [6:36]: An error notification to to slide. So, now I'm gonna save that and publish it.

@Matthew Kerns [6:39]: Nice

@Trent [6:44]: Change to the publisher, that's fine. But I need to unpin this I think. Because of changes in the workflow, output data may change when this node is grown again. That's fine.

@Trent [7:02]: OK. It's fine. There's no publish to do. OK, so then, and I'll have Claude Code pull down the the ones that I have in here. So like if I just made a change there, right? I would

@Matthew Kerns [7:16]: Mhm

@Trent [7:17]: I would pull down from cloud coat or use cloud code to pull down the workflow. so then, The, I showed you call summary, I showed you error handler. The way the air handler works is inside of quote ignore the quote transcript in the table notes, OK, so the quote a job or request is what's in the repository.

@Trent [7:39]: This one here

@Matthew Kerns [7:40]: Mhm

@Trent [7:40]: Well, all three of these are that I've mentioned. It looked, I just made a change here, so it's a little bit messy. Let's clean it up. OK. So, it looks like it's trying to inject Like, I wish it would have used a better node situation than this. This is one of the problems with cloud code. I kinda wish it had a better idea of what nodes to use.

@Matthew Kerns [8:04]: Mhm

@Trent [8:05]: It's trying to generate a some AI summary, I was just now telling it that I wanted to use Gemini. To Create the summary, but I kind of wish it would have just used the agent node, so I would probably go in here and manually modify this.

@Trent [8:24]: To the way that I want it

@Matthew Kerns [8:24]: Yeah Yeah. So we don't have an LLM hooked up yet anywhere in these notes or work.

@Trent [8:31]: I don't have, yeah, correct. I don't have anything in this workflow at all connected to an LLM. It literally is on the left hand side. It's just a web hook. And this web hook is set up in quo right now. If you go to quo, go to settings.

@Matthew Kerns [8:40]: Mhm

@Trent [8:46]: Go to webhooks. This, well this is my webook right here. You can add one for yourself, so you can run your own sandbox and hit create webook and do the same thing.

@Matthew Kerns [8:56]: Yup, got it

@Trent [8:57]: OK? And then inside of here, I just have it. I'm not using the secret. I'm just letting it send it. That's just so like, if you want to authenticate the webook, right? The message that comes into NAN.

@Matthew Kerns [9:10]: Yeah

@Trent [9:11]: I'm not, I'm not authenticating it at all. I'm just letting it come in.

@Matthew Kerns [9:14]: OK

@Trent [9:16]: But you can select your call mess like I selected Transcript, summary, message received, and message delivered. I decided not to collect completed ringing and recording. Currently

@Matthew Kerns [9:29]: Mhm.

@Trent [9:31]: Because I was more focused on this aspect of it.

@Matthew Kerns [9:35]: OK

@Trent [9:36]: But these are could be useful at some point in time.

@Matthew Kerns [9:40]: Mhm

@Trent [9:41]: If it's bringing, we want to see the number, we want to respond to the phone number, whether or not it's a particular contact We could send back using API until to do something with it. Right

@Matthew Kerns [9:53]: Yeah, ahead of time so that we might be able to improve the quality of something. But not yet

@Trent [9:59]: Yeah, like if we had a contact list of people that needed to be routed directly to Kelsey, we could use that list and we could respond to it.

@Matthew Kerns [10:09]: Mhm

@Trent [10:09]: Right? Yeah

@Matthew Kerns [10:11]: Yeah

@Trent [10:11]: Because you can you can force an action to using an API. So. For routing So anyway, I did that and I did updates on All phone numbers. There's only, there's two phone numbers.

@Trent [10:29]: So you can basically, what you can do is for the webhook, you can pick up one particular phone number if you want to, or you can just say all.

@Matthew Kerns [10:37]: Mhm.

@Trent [10:38]: And then I actually have it set up for contact updated and deleted, I'm capturing those, I guess, but I haven't seen them yet. I haven't been messing with that aspect of it. So, so anyway,

@Matthew Kerns [10:53]: Right. And then, so you can, you can also set up different web webhooks for different event types.

@Trent [10:54]: That's Correct. So if we wanted to, I actually did this at first. I set up just one web hook for transcripts, and then I was going to set up another one for summaries, and I was going to set up another one for messages, right?

@Matthew Kerns [11:07]: Yeah Yeah

@Trent [11:16]: Yeah, and we can, we can respond. You just create another webook. I don't know what the limit is. Right, on how many you can create, but I mean, you don't really have that many possibilities. So I don't think it's a limitation. Here's the events log, so these are all of the web hooks that have been sent so far, and you can see the response, the response is our response from NAM. So when it sent it, we got a response back and it's 200. That means it's all good.

@Matthew Kerns [11:41]: Mhm.

@Trent [11:45]: You can also look at the event details if you want, and you can hit retry request. So if you want to test something from quo. To N8N, you can just hit retry request.

@Matthew Kerns [11:56]: Oh yeah, I was wondering how you were doing that. You were showing that earlier. I was like, that's so cool. How do you do that? But now I get it.

@Trent [12:01]: Yeah, so this is what happened last was a summary was completed. So now if I hit request It'll retry and it responded, but now if I go in here, if I were to look at executions, you'll see that this succeeded.

@Matthew Kerns [12:10]: Yeah. That's like such a quicker iteration than like other ways, so that's good.

@Trent [12:19]: Oh, I know. Yeah, so I like quo for that. I mean this is like really easy to to iterate on, right? So,

@Matthew Kerns [12:26]: Yeah.

@Trent [12:27]: I mean, that's the one that just came in. So what, if you follow this flow See if I can zoom in. Yeah, I can. OK. if you were to follow this flow at the very beginning, what's happening here at the beginning is Webook comes in, we parse it, we're just kind of

@Trent [12:45]: Putting it in the format we need, logging it to a table and then it's cleaning up old logs, so it's just looking at anything that is 30 days old.

@Matthew Kerns [12:47]: Mhm.

@Trent [12:56]: Anything that's

@Matthew Kerns [12:56]: OK.

@Trent [12:57]: Anything that is Conditions Row, delete Delete if created at Is less than 30 days. Now minus 30 days.

@Trent [13:16]: That's that

@Matthew Kerns [13:17]: We might not want to do this.

@Trent [13:22]: And that's fine. I just

@Matthew Kerns [13:22]: But Yeah Yeah, yeah That's fine. I'm just saying like But I don't necessarily, I'm, I'm not saying like I'm gonna delete it right now cause I don't think that's priority. Like it's, it's kind of fine, but I might make a notion task to move it to another workflow or something.

@Trent [13:44]: What are you thinking on that? Because you, you, we can't just keep pumping data into the database and just leaving it there forever.

@Matthew Kerns [13:53]: Right?

@Trent [13:54]: 30 days, 1 year.

@Matthew Kerns [13:59]: I think we need to Well, we need to figure out a strategy for that. So,

@Trent [14:08]: And then do we want, then do we wanna take do we even want to take responsibility for it even being here. Because it is like user data, so

@Matthew Kerns [14:20]: Yeah, I mean, I mean, yeah, we've maybe for now we just leave it. I just think at some point, we're gonna want to make sure we have a strategy. Maybe it's by the time we hand off

@Trent [14:21]: Yeah.

@Matthew Kerns [14:33]: The phase one deliverable. But So,

@Trent [14:37]: A strategy of long-term storage, right?

@Matthew Kerns [14:41]: Yeah

@Trent [14:42]: I was just thinking this was a log for us to be able to go in and look at stuff.

@Matthew Kerns [14:47]: Yeah

@Trent [14:48]: Not infinite storage, right?

@Matthew Kerns [14:48]: Yeah Yeah, not like, we don't, OK, so we don't need historical sort of data yet. We also need to think about how are we handing off the NAN workflow, or like, we'll we'll be managing it for a while, assuming that they, I mean, yeah, we got to think about that later, but

@Matthew Kerns [15:07]: Anyways.

@Trent [15:08]: Yeah, but, OK, so, And then it's just right here, it's checking to see if it is a transcript or not.

@Matthew Kerns [15:19]: Mhm

@Trent [15:19]: So if it's not a transcript, it just responds back to quote telling it received the web hook. Cause you gotta to respond

@Matthew Kerns [15:28]: Mhm.

@Trent [15:29]: If it is a transcript, it runs through the process, and the process is extracting, searching job or client, It wants to see if Joer has a client that matches. If the client exists, then If it exists, then just get the client ID.

@Trent [15:48]: We already got it back here cause we looked it up. If it doesn't exist, then create it.

@Matthew Kerns [15:56]: Yup.

@Trent [15:58]: And then search for open requests, so it's looking in the requests area of jobber to see if there is an open request that matches this Contact

@Matthew Kerns [16:10]: Mhm

@Trent [16:11]: Checking it And then let's clean, well. It's becau it's a messed up right now because let me just go back to the editor. It's it's clean now

@Matthew Kerns [16:25]: Maybe it was like that in the execution, so that's why it got That's why it went that way, but

@Trent [16:29]: Yeah Yeah, it captures what the current state was, yeah.

@Matthew Kerns [16:34]: Yeah

@Trent [16:34]: So if you make changes in between executions that you'll see the changes in between.

@Matthew Kerns [16:39]: Mhm

@Trent [16:41]: Or in between each one. So, but anyway, so now this is new stuff. The new stuff is to generate the AI summary, which is not Functional, has not been tested at all.

@Matthew Kerns [16:52]: So new meaning from today, like so if you're working on today.

@Trent [16:55]: Like, like, yeah, in the last, I don't know, hour or 30 minutes or something. So

@Matthew Kerns [16:59]: OK

@Trent [17:04]: But the AI summary is new.

@Matthew Kerns [17:08]: Mhm.

@Trent [17:09]: But the creating a new request, adding note to new request. Add new, add note to existing requests that those paths Were all Already there. So

@Trent [17:25]: To really, this is the only thing. And it might, it's feeding into these, because I'm trying to get it to where it uses this information from the summary to append it or create the note.

@Matthew Kerns [17:39]: Mhm Got it So this is

@Trent [17:43]: So,

@Matthew Kerns [17:47]: Basically Sort of trying to redo the quota jobber integration, but we need that because it does, the, the existing one doesn't capture everything like voicemails, right?

@Trent [18:01]: Right, it doesn't assign the contact name and it doesn't capture voicemails, and it doesn't capture messages. And it doesn't

@Matthew Kerns [18:11]: What are messages

@Trent [18:13]: Texting

@Matthew Kerns [18:15]: OK

@Trent [18:16]: So like when you text a client back and forth.

@Matthew Kerns [18:21]: From quo and back and forth, and then does quote and then quote on the web hooks, do they give us they give us those events.

@Trent [18:24]: Correct Yeah.

@Matthew Kerns [18:31]: OK.

@Trent [18:33]: Yup. We get those events. If somebody texts in or you send out, you get those webook events.

@Matthew Kerns [18:42]: Cool.

@Trent [18:43]: But you can see on the right-hand side, this transcript here doesn't have like a contact name in front of it or anything or a phone number. It's just the text. On each line

@Matthew Kerns [18:56]: Mhm

@Trent [18:57]: So that was something I was trying to address because if you go and look at the job or account. You look at Kelsey's job account. You'll see that it has a phone number, like this, and in brackets.

@Trent [19:15]: And it just does phone number and then the next phone number. Then the next phone number, then the next phone number. So it doesn't even use the contact info. So I was just gonna try to see if since I was already trying to Acquire the contact info stuff.

@Matthew Kerns [19:31]: Mhm

@Trent [19:31]: I was just gonna see if I could just assign At least assign the names of the plotter mechanics people. Like Kelsey this and phone number says this.

@Matthew Kerns [19:44]: Yeah

@Trent [19:44]: I, right

@Matthew Kerns [19:47]: Yup. OK

@Trent [19:50]: Is what I

@Matthew Kerns [19:50]: So that was the next thing that one of the next things you were working on?

@Trent [19:54]: That was something that's supposed to be in this. Supposed to be in this here. It's supposed to already be doing it, but I have not tested it. I don't know. If it works or not

@Matthew Kerns [20:03]: Oh, I see Cool

@Trent [20:06]: Don't know what the outcome is right now. I don't know if I can.

@Matthew Kerns [20:08]: Yeah.

@Trent [20:18]: Because I haven't done this integration yet. It won't function

@Matthew Kerns [20:25]: Well Well, if we're not gonna be using that HTTP requests, no long term. I might just Swap it out now And then

@Trent [20:36]: Yeah, that's fine. That's what I'd do

@Matthew Kerns [20:38]: Yeah, OK, and then like tests that way.

@Trent [20:41]: Yup

@Matthew Kerns [20:42]: Cause there's gonna be errors there and then, yeah.

@Trent [20:44]: Yeah, I would probably just tell Claude Code, hey, look, I don't want to use the HTTP request. I want to use the agent node and have it figure out how to make the changes. Because I don't know when you

@Matthew Kerns [20:55]: Yeah

@Trent [20:57]: I don't know what all is coming out of this. What, it's doing on the other side, right? And look at that, I mean, it's doing some JavaScript, right? So I don't, I don't wanna spend my time digging through that, so I would just be asking Claude Code to figure it out.

@Matthew Kerns [21:16]: Yeah

@Trent [21:17]: Just giving it specific direction to use, like,

@Matthew Kerns [21:17]: Makes sense.

@Trent [21:22]: Like either use

@Matthew Kerns [21:25]: Yeah, the agent, the AI agent model, and then The Gemini chat model. As part as the model Component of the agent

@Trent [21:37]: So it looks like there's audio actions even in here too. Transcribe, I analyze audio, document, file actions, text actions, so you can message a model if you want to just do it that way, right? But Again, that's let's just so like right there is just a direct Gemini.

@Trent [21:58]: Node for messaging a model. But then, right, there's a an agent node too, right? This one here.

@Matthew Kerns [22:02]: Yep Yeah

@Trent [22:07]: Which is more universal

@Matthew Kerns [22:10]: And might be overkill if we're just want a, a, an AI summary, so I'll think about that.

@Trent [22:16]: Yeah Yeah, I was just thinking probably just do this, and just use like, the simple, cheap, lowest

@Matthew Kerns [22:21]: Yeah

@Trent [22:25]: Model or something and see what we get out of it,

@Matthew Kerns [22:28]: Mhm.

@Trent [22:30]: Is all I was thinking, like was it 2.5 flash or something. Flash Mini or something like that

@Matthew Kerns [22:36]: Yeah

@Trent [22:36]: It won't, it won't show anything because I don't have a credential in here, but

@Matthew Kerns [22:37]: I that

@Trent [22:44]: But That's kind of what I was thinking anyway. And then I was gonna just Curious what it did in here. So it's got a It's got a prompt in here.

@Trent [23:01]: Analyze this phone call transcript for blotter mechanics, the plotter company, blah blah blah, in Phoenix extract call summary. Next steps, equipment, And there's some examples in there.

@Trent [23:18]: But we could get those examples from somewhere else, right? We could inject a list of them that we

@Matthew Kerns [23:24]: Yeah, so that's

@Trent [23:24]: Pull from somewhere

@Matthew Kerns [23:26]: So I pulled From Plotter Mechanic's website, a bunch of data and created that knowledge base file so I can hook that up.

@Trent [23:34]: Yeah Yeah, we could do that too, right? We could just bring that in just so we can see how well it works and then we could just continue to iterate until we get it to where it's the most manageable and flexible version that we feel like We feel satisfied with, I guess. So,

@Matthew Kerns [23:51]: Yeah, I think that's one of the main things that would prevent further adoption is making sure that The transcript is reliable, so I want to focus on that, making sure we get high quality Inputs to our, to my, to our trial jobber accounts with the transcripts.

@Trent [24:12]: Yeah, exactly, and that's what I'm thinking too, and if you go in and look at the quo account, there are some good examples in there too, so go to the primary and you could click down through here some of this stuff. and you can see

@Matthew Kerns [24:22]: Nice.

@Trent [24:28]: That Yeah, so if for any reason you need to like market

@Matthew Kerns [24:32]: That

@Trent [24:35]: Red or unread, you can do that here. Like if for some reason

@Matthew Kerns [24:38]: Should I though

@Trent [24:40]: What?

@Matthew Kerns [24:41]: Should I, it's not, I guess it's not part of their workflow yet, so I guess I could.

@Trent [24:45]: So what happens is they, Kelsey knows that he can go into the Quo app and see the latest calls, but my point in telling you that is that if you open one of these up and for some reason that bubble goes away, you can just click the button to put the bubble back.

@Matthew Kerns [25:03]: OK

@Trent [25:03]: That way, that way it doesn't chase state on Kelsey.

@Matthew Kerns [25:07]: Yup, got it

@Trent [25:08]: And Joer has the same situation, so if you could see the text messaging app, but you can't right now. Do you want to see the text messages, you can click into it, and you can open the text message. And then it got the red bubble, like whether it's been red or unread, goes away, but then you can mark it on red when you come back out of it.

@Matthew Kerns [25:20]: OK. Mhm. Yup

@Trent [25:31]: So But, but yeah, so the, the quo Here's the, so if I were to log out of this real quick. There's my. Oh And log in as

@Trent [25:48]: Plotter mechanics To from a keyboard By login under my This is the plotter mechanic's account. So,

@Trent [26:05]: If I were to look at, let's say requests, and you look at an example request. See this is what they're getting, right? but you look at one of these, And what you got on the right, you see how it's got the bracket with the numbers.

@Matthew Kerns [26:22]: Mhm

@Trent [26:23]: At a minimum, it would be nice to just say like this number is known. This is Kelsey. So, at a minimum, we should be able to just put Kelsey in here.

@Matthew Kerns [26:31]: Yeah

@Trent [26:36]: Right? Regardless of what the other number is, we could just leave the other number alone if we want to. Because if they change the name in here for any reason, it won't match.

@Matthew Kerns [26:43]: Mhm

@Trent [26:48]: The transfer to the right. So,

@Matthew Kerns [26:48]: Right Yeah

@Trent [26:51]: But here it says, my name is Reed.

@Matthew Kerns [26:52]: Yeah

@Trent [26:54]: Right?

@Matthew Kerns [26:55]: Mhm

@Trent [26:55]: So what, right here, I'm calling from here. Right? So why can't we pull that stuff out?

@Matthew Kerns [27:00]: Yes

@Trent [27:04]: You know what I mean? So

@Matthew Kerns [27:07]: Right

@Trent [27:08]: And then, but it, but look here though, this one's

@Matthew Kerns [27:10]: It's a cool

@Trent [27:11]: Go ahead, what

@Matthew Kerns [27:12]: Where, where will it go once we pull it out? Is it Can we attach it to the request in a field?

@Trent [27:19]: Yeah, we can, yeah, we can just put it where, where we want. We could put it as a note or the idea is that we want to do something like this. See how this says a call summary and next steps.

@Matthew Kerns [27:29]: Yeah.

@Trent [27:29]: If you go, if you go look at quo For this phone number 3757 So 3757.

@Trent [27:47]: Or read right here. So it picked out his name. Interesting that it picks up the name, but you actually have to come in here and click save to Contacts for it to go into the contexts list.

@Matthew Kerns [27:59]: Yeah, I mean,

@Trent [28:00]: And you You, you don't give any of that info, but you don't get any of that info in the webook.

@Matthew Kerns [28:02]: We might Right, OK, so we don't get contact suggestion info.

@Trent [28:13]: Nope.

@Matthew Kerns [28:15]: And

@Trent [28:15]: You'd have to take it on yourself, just like what they're doing. They're, they're picking out the name from the transcript.

@Matthew Kerns [28:18]: Yeah So, OK, so I think we should sort of Document Like keep track of all the stuff that Is like manual steps, so like

@Matthew Kerns [28:37]: They probably do that for a reason, like, OK, we're not like a lot of the times the name just, it just gets the name wrong. So that's why there's this manual step.

@Trent [28:48]: Yeah.

@Matthew Kerns [28:48]: To make the AI using the AI less annoying because we need to make sure that it's not annoying to use whatever we give to them or and like that's where our SOPs are going to be critical because we can just say like hey this is this is the annoying part. This is a manual step that you need to do. It's going to be faster than before, but you still got to do this manual.

@Trent [29:12]: Exactly, yeah, we're definitely gonna have those cases that we're going to have to show them what to do, right? Cause it's just like saving the contact to his if he has it in his phone, it synchronizes it to hit the contact list in quo, but the thing is, is none of that ends up in Jaber

@Trent [29:32]: So,

@Matthew Kerns [29:34]: So it existing contacts don't, don't end up in Jaber.

@Trent [29:39]: So Correct That's correct

@Matthew Kerns [29:43]: Like the client and stuff.

@Trent [29:43]: Existing contacts that are in his phone Have to be manually input into job or some way. Like right now, if this was if this contact was in his phone, it would still come across as new call some number, and then Alyssa has to go in here and add the details for the

@Matthew Kerns [29:51]: Mhm

@Trent [30:04]: Client

@Matthew Kerns [30:05]: Got it So we can

@Trent [30:07]: If they're not, they don't already exist.

@Matthew Kerns [30:10]: Yeah I almost, I almost kinda wanna do like just a, an audit, make a definition, make a document of like What Like if we did nothing What would Alyssa need to do manually, and then

@Matthew Kerns [30:27]: Like what can we do? And And then kind of plan our Quality from there. I know you've already done a bunch of this, so like, Like, mentally like just

@Matthew Kerns [30:45]: In your head And I'm sure, I don't know like what other planning you did though with Claude and whatnot, but

@Trent [30:52]: Yeah, I yeah, I haven't really done much other than what we're talking about here. If you go look at notion, you'll see the outcomes of what I've done so far. Whatever's in notion, like the issues list And the task list are the two primary things you would want to look at.

@Trent [31:11]: But otherwise, it's what we're looking at here. I'm trying to

@Matthew Kerns [31:11]: But

@Trent [31:16]: Get parody. Between what we're trying to achieve and what Quo already does, but then enhance it with the contact info.

@Matthew Kerns [31:19]: Yeah

@Trent [31:26]: And I figured if I'm getting the contact info already, why not just ask the agent in the same prount. To extract any printer models that identifies.

@Matthew Kerns [31:37]: Yeah.

@Trent [31:38]: Why not ask them You know what I mean

@Matthew Kerns [31:41]: Yeah. Yeah, like all the data that's available in the transcript, we should parse out.

@Trent [31:46]: That that matters, right? Anything that like is specifically Notable To plotter mechanic's business.

@Matthew Kerns [31:55]: Yeah, one Thing to consider might be Multiple, like one node per Thing that we want to extract, like, not per field, but like

@Matthew Kerns [32:14]: Just Instead of, so, like, doing extracting everything at once. There might be more inaccuracies for like here and there, then if we extract Chunks that mean the same thing.

@Matthew Kerns [32:32]: Across different nodes, so it's just something I'm think.

@Trent [32:36]: Yeah, I see what you're saying, yeah. So we might have to do a preprocessing step, and then break it apart and then take those pieces and then do a a post process or something, right?

@Matthew Kerns [32:48]: Yeah, maybe so, or like when I, when I'm thinking about the meeting transcripts and things like some of these meeting transcripts that we have internally are just super long. So, but if I come from it like, OK. I want to extract things from this Elissa recording that are specifically related to roadmap items.

@Trent [33:09]: Oh God

@Matthew Kerns [33:09]: Then I'll do prompt, and I'll do extract roadmap from the full transcript, right? And then if I wanna do like, OK, let's extract details that where I can update my notion tasks, let's do that, then we'll do, I'll do a separate prompt.

@Trent [33:26]: Correct, you might do it in a separate prompt because when the agent is taking your prompt, it's coming from a different perspective, right? So, you may not get the same results by doing a single prompt for a specific task, as you will by giving it a long

@Matthew Kerns [33:35]: Yes

@Trent [33:43]: Multi multitask, but I don't know. I think, I think it would be worth just trying it in one and maybe testing it the other way, because we do pretty long prompts for a lot of things in Cloud Code.

@Matthew Kerns [33:46]: Exactly Yeah.

@Trent [33:57]: And it figures it out. So

@Matthew Kerns [34:01]: Yeah. I, I think that for the big long transcripts like our meeting. Ones, it's probably more likely that that's an issue. because it will just think like, OK, I should go abroad, make sure I fulfill the customer's request, but I don't necessarily, like,

@Matthew Kerns [34:19]: If the request is a single concept, then it can go really deep. With that one

@Trent [34:26]: Right. Right

@Matthew Kerns [34:28]: But yeah, for this, it's like way shorter transcripts, so depending on the model, And the prompt sophistication. We can refine things that way.

@Trent [34:42]: Yeah

@Matthew Kerns [34:44]: Yeah, we will need to also do some cost assessment, but yeah, I think, OK, I'm like I keep going off onto other things that are going to be later, but for now we just want to reach parody

@Trent [34:54]: Well.

@Matthew Kerns [34:58]: Right?

@Trent [34:58]: I'm trying to reach parity with if I'm doing, if I'm doing the work to reach parity, and I can go ahead and just throw in a a slight enhancement. While I'm there, I'm doing it, you know what I mean?

@Matthew Kerns [35:10]: Yeah

@Trent [35:10]: But Not like feature ad necessarily like it requires a bunch of extra effort, but if I can just put it in the prompt For the AI to do it, I'm just gonna go ahead and just try it out.

@Matthew Kerns [35:23]: Yeah

@Trent [35:24]: But one thing to know if you're talking about the cost analysis was he's used 300 credits out of 1000 already. If you look at the usage rates, it talks about here that it Sona calls, costs 100 credits per call.

@Matthew Kerns [35:33]: Mhm

@Trent [35:40]: So if you were to go back and look at his calls. I don't know if the analytics

@Matthew Kerns [35:46]: Which ones even use Soo? I thought we didn't work

@Trent [35:49]: Only when Sona is like taking a call, answering a call, and SONA is enabled. So

@Matthew Kerns [35:56]: And we disable it

@Trent [35:57]: We can, yeah, like right here, Sona, this is the current call flow, Sona call flow, it answers right there. So, as far as I know, We could just not use sonar, and it doesn't, it won't Cause any

@Matthew Kerns [36:12]: Yeah

@Trent [36:13]: Overage

@Matthew Kerns [36:14]: I think that's, I think we should do that as soon as possible. did he, who set this up though? Did he set it up?

@Trent [36:21]: No, this is default. This is just out of the box.

@Matthew Kerns [36:24]: Oh OK.

@Trent [36:26]: No nothing has been done in these at all. So, if we're gonna reach feature parody with

@Matthew Kerns [36:31]: Yeah

@Trent [36:36]: Well, so here's the thing, When I talked, so we have it in our task list, which I did not update this yet, but We have it in our task list to merge the Vonage Menu options over, like to reach parody with the menu.

@Matthew Kerns [36:56]: Yeah

@Trent [36:56]: But, but when I talked to Kelsey, he said, well, we don't have a line for each person yet. He's like, do we, and then we talked about, oh, who, who needs a line? And I explained to him what we had already determined that Joni's line, Alys need the line, and Nicky does not need a line, I already told him that, and he agreed.

@Trent [37:19]: And but he said for now, he wants everything to go through quo. And he wants to be the person that is fielding the call, and he right now what he's done is he's given a list of instructions. That if it rings 4 times, That she needs to pick it up

@Matthew Kerns [37:39]: OK

@Trent [37:40]: And that's, that's how they're handling it currently.

@Matthew Kerns [37:40]: Yup

@Trent [37:44]: He knows that's not the final thing, but he wants us, he wants to get all the data in quo as much as possible.

@Matthew Kerns [37:44]: Yeah Yeah. I think, I think we definitely got to turn off Sona because we wanna make sure that that stays the case, like he, like we want him feeding all the data through quo, and if he starts getting a charge, he might have reservations.

@Trent [38:07]: Well, here's what I can tell you is that there is a feature in the settings. That lets that allows or disallows the overage. So if you go to the plan and billing, there's a Allow overages setting. It's currently disabled, so it's not going to charge him any more.

@Trent [38:27]: But I don't know what happens when he runs out of credits.

@Matthew Kerns [38:32]: Yeah

@Trent [38:34]: Like to the client, if for any reason the Sona goes to answer the call, what is gonna happen? I don't know.

@Matthew Kerns [38:41]: Yeah.

@Trent [38:42]: We'd have to research that, but it won't charge him anymore, so The way I'm gathering this is it's just going to stop with Sona at 0 But here's the thing that I was thinking about was if we put the menu system in here.

@Trent [39:05]: It is gonna forward or redirect the calls to phone numbers that are not in, quote, So, we can't do that right now. We can't do that until we add a new line for Alyssa and a new line for Joe.

@Matthew Kerns [39:27]: I mean, could we do a menu system and then just not redirect the phone number so that the customer still sees The menu system like they do in Vonage, but it still goes the same number and then he can well if it ranks 4 times, Alyssa picks up.

@Trent [39:49]: New call flow. Phone menu So there's the phone menu. If the phone menu, you can do the greeting, you can press 1234. So if you do one and then add another option, so now there's 2

@Trent [40:09]: 1 and 2 It'll ring users. Basically, that's what the default is anyway, right now. So if you just, if you add one, all it does is it just rings. You press 123 or 4 or 5.

@Matthew Kerns [40:16]: Yeah

@Trent [40:22]: It doesn't matter, it just rings the users.

@Matthew Kerns [40:23]: Yup

@Trent [40:26]: The only, the only thing I would say is that currently, Kelsey wants to be fielding all the calls. He wants to answer all the calls.

@Matthew Kerns [40:26]: Right

@Trent [40:34]: So if a call comes in and we have every call go through the phone menu. It's gonna disrupt that flow. So I, I'm, I'm currently in a place where I think we just leave it alone Until we have all of the lines.

@Trent [40:53]: Available And I mean

@Matthew Kerns [40:56]: But So, sorry, can you say that again? I was thinking about something.

@Trent [41:01]: That's fine. So, I don't think we need to put the menu system in here. Until they Have all lines for Alyssa and Joe and Kelsey. And we're waiting on the port. We're waiting on a port too.

@Matthew Kerns [41:17]: Oh

@Trent [41:19]: So

@Matthew Kerns [41:20]: Yeah, so wait, how come We can't just ring the users with like with the default one, So that we can, cause we can get the customer facing parity with the menu, and then it is redirectable one, yeah.

@Trent [41:36]: Well, all the pull on. Hold on, I'll stop you there. Stop you there.

@Matthew Kerns [41:40]: Yeah.

@Trent [41:41]: We can't because the, the customer facing parity is two channels. It's either the office number or it's Kelsey's number. Currently, they're both going to one phone number

@Trent [41:57]: In o And we can't respond to those differently. So, the current situation be sorry, not current, before quo Vonage was the only menu system they had.

@Trent [42:14]: And I looked at their history, their call history. I, I downloaded it, their call log. They only had 8 calls in the last 3 months.

@Matthew Kerns [42:25]: OK

@Trent [42:27]: So, it's not even really

@Matthew Kerns [42:30]: Yeah

@Trent [42:31]: A thing So most of them all go to Kelsey anyway.

@Matthew Kerns [42:33]: Yeah Yeah, yeah, yeah, like I mean just like, OK, well, I'm not even gonna think about that anymore then they call.

@Trent [42:39]: So Yeah, I, yeah, I.

@Matthew Kerns [42:44]: They're like 20 calls a day here, so.

@Trent [42:47]: Well, yeah, I mean, yeah, just yesterday, he had like 20 calls or yeah 20 calls a day and he had like 16 yesterday. So, I mean, he got 36 calls in the last two days.

@Matthew Kerns [42:59]: Yeah, dude, and those numbers, that, that's, dude, I love to hear that because that's like, We can Get some of those called, like we can get 80% of those calls off his plate. He is going to love us, first of all, and his time's gonna be freed up, so

@Matthew Kerns [43:16]: I really want like a, I think Now we have A lot better idea of the requirements that we're trying to deliver by next week, and I think that we should Put together, I might even just focus on that tonight. Just put together a detailed requirements document, like what are all the line items that we're trying to deliver.

@Trent [43:42]: That's fine. Yeah, that's fine. just the only thing I My in my insides, like my brain and my heart are just telling me do do do. Instead of planting plan, so, I mean, I, I'm all for, you know, trying to document that and trying to make sure we understand it,

@Matthew Kerns [43:55]: Yeah Yeah

@Trent [44:05]: But

@Matthew Kerns [44:06]: I just wanna make sure that I'm not doing things that we're not gonna deliver in the end. Like I don't, I really don't want to waste time, so I wanna have a clear picture of like, what are the requirements for this phase and why are we delivering those and then as soon as, but like also as soon as I have

@Trent [44:24]: Yeah

@Matthew Kerns [44:27]: One or two of those, it's build, build, build, right?

@Trent [44:31]: Yep, yep. I, I say if that's something that you need to do and you don't feel like it's clear enough now, then yeah, go, go do it. go look in notions, see where we're at with use cases, 12, and 3. And I think there's duplicates in there. There's like 2 1s and 2 2s or something, but regardless, but the use cases, look at the look at the issue items and look at the tasks, just kind of look at all those together a little bit, the use cases are short. It's like there's like 5 of them or something.

@Matthew Kerns [44:42]: Mhm

@Trent [45:02]: And the, the things below them are the issues and the tasks.

@Matthew Kerns [45:02]: Yeah

@Trent [45:05]: And then just look at those and try to get an idea on what you think we're really delivering and You know, look at the PRD to understand what the PRD is saying that we're trying to solve. And I, I keep coming back to if we can just make quo a jobber work really well.

@Matthew Kerns [45:17]: Yeah.

@Trent [45:23]: They'll they'll be happy with it. So,

@Matthew Kerns [45:23]: Yeah Yeah, cause the handoff case, it's kind of like

@Trent [45:32]: It's almost solved if we can just get the, these communication patterns. Handled

@Matthew Kerns [45:39]: That

@Trent [45:40]: In an automated way

@Matthew Kerns [45:41]: Yeah, exactly, like he doesn't need to do the handoff anymore if it's all recorded.

@Trent [45:46]: Well, that's what he was

@Matthew Kerns [45:46]: Boom

@Trent [45:48]: He was acknowledging that, that just the built-in integration of quote to jobber is already helping him.

@Matthew Kerns [45:50]: Yeah Yeah, yep So now we're just kinda cleaning stuff up, making it as good as you can.

@Trent [46:01]: Yep That's the way I see it is that Like right right now somebody's calling. But that's the way I see it is that It

@Matthew Kerns [46:13]: So that's going to sauna

@Trent [46:16]: Let's see, is it? You didn't answer. Kelsey Took a call earlier or something?

@Trent [46:37]: Yeah, 5:45. I don't know. I don't know if I read that way, but regardless, So that's the way I see it, is that if we could just make this work better for them, so that like their complaints when I was talking to Kelsey, right, was that

@Trent [46:56]: The contact you still had to put that in. And I figure if we can get the contact right, we can get the messages and the voicemails to go in And if, while we're at it, if we can show them that we can pull out specific things using AI that are valuable to them, that they're looking for.

@Matthew Kerns [47:16]: Mhm.

@Trent [47:17]: I mean I think that, you know, that's all I wanna say low hanging fruit, but

@Matthew Kerns [47:26]: Yeah, but the reality is it takes longer than we think, always, but.

@Trent [47:30]: Everything does, yeah, everything does. But the

@Matthew Kerns [47:33]: Yeah

@Trent [47:34]: I think we just focus on trying to get this right.

@Matthew Kerns [47:34]: But

@Trent [47:37]: I think that

@Matthew Kerns [47:38]: Yeah

@Trent [47:39]: He'll be satisfied

@Matthew Kerns [47:44]: Can be That's actually impactful. To their workflow

@Trent [47:54]: Yeah, exactly, that's kind of, I think this is going to be an impact for the workflow because they, they spend so much time With the phone calls And it, they just need the the Anything we can get automatically and do for them in Jaber using these phone calls. That's

@Trent [48:11]: A huge help

@Matthew Kerns [48:13]: Yeah, cause that, because that will reduce The amount that Alyssa needs to go in and manually do.

@Trent [48:23]: Yeah, so the manual hand

@Matthew Kerns [48:23]: And if she has that

@Trent [48:25]: Are reduced

@Matthew Kerns [48:28]: The manual what or reduce

@Trent [48:29]: The the handoff, the handoff calls between her and Elsie is basically almost not needed at all.

@Matthew Kerns [48:32]: Yeah. Yeah, then she can, ideally, she could just Look the requests, have all the data there, and Move it somewhere

@Trent [48:47]: Yeah. Exactly, she just does what she needs to do with it. She processes it.

@Matthew Kerns [48:49]: But Yeah, I I also am thinking though that like, There needs to be some, there needs to be a high level of confidence. With that. Otherwise

@Matthew Kerns [49:05]: Cause if Say if the automation gets the name wrong. Like a few times. The reality is, like, even if we get if it gets 3 out of 100 wrong, she might end up going and playing back the voice, the recording of it, just to double check to make sure you get the name right cause it's like, you don't wanna say the wrong name, you don't want Kelsey to say the wrong name.

@Matthew Kerns [49:31]: And then he comes back and tells Alyssa, like, what the heck? Like, you told me the wrong name. We have the recording. So

@Trent [49:41]: Right. Right

@Matthew Kerns [49:43]: I wanna still work from like What is the SOP that Alyssa would follow right now.

@Trent [49:52]: Yep.

@Matthew Kerns [49:52]: And then let's see what we can realistically optimize and what are the risks associated with if it gets it wrong, then, and then we can do testing.

@Trent [50:01]: Yeah

@Matthew Kerns [50:04]: Get some data on like, like how accurate can we get this?

@Trent [50:09]: Yeah Exactly. And I, I noticed something, I don't know, like the requests are disappearing.

@Matthew Kerns [50:18]: Hm

@Trent [50:18]: So, I think she's Converting them and then deleting them.

@Matthew Kerns [50:26]: OK

@Trent [50:27]: I don't know if she wants to do that.

@Matthew Kerns [50:31]: Got it

@Trent [50:32]: I mean, like, that's what she's doing, but I don't think that's what we want her to do, if she keeps doing that, they lose this call history.

@Matthew Kerns [50:41]: Yeah, they lose the notes.

@Trent [50:43]: I'm pretty sure the notes get lost.

@Matthew Kerns [50:46]: So the sooner we can get them an SOP on like what we know. We can literally deliver that and then that way, Instead of them running, like they're gonna run into that issue at some point soon, like maybe tomorrow, and then It's gonna be like, hey, the notes are missing now. What happened? And they might ask us, you know, cause they just don't know.

@Matthew Kerns [51:10]: And then it would be cool if we could come to them with an SOP and be like, here's how you're supposed to use it, and now we're delivering on our promise, right?

@Trent [51:18]: Yeah, exactly. I think that's a good, that's a good plan. But yeah, I think she's, I mean, I don't know how many have come in through the requests. But

@Matthew Kerns [51:29]: Got to be more than 5, right

@Trent [51:31]: So if I go to the que requests and if I go to you can change the status to only converted ones. And there's 99 of them, but it's not sorted. So if we look at the most recent ones, See, look here There's only one converted right here.

@Matthew Kerns [51:50]: Yeah

@Trent [51:51]: So, if I click on this one It has call history

@Matthew Kerns [51:55]: Yeah

@Trent [51:57]: And it's been converted to a job. I'm pretty sure if you wears the job. You click here job 1819. And then you scroll down, you'll find that the history. Right

@Matthew Kerns [52:09]: Yeah

@Trent [52:11]: But I know she's been putting more things in than that.

@Matthew Kerns [52:14]: Mhm.

@Trent [52:15]: Or one So

@Matthew Kerns [52:19]: Yeah Cool

@Trent [52:26]: So anyway, OK, so just coming back to like if you want to work on it, what I'm gonna do is I'm gonna have Claude Code pull down the latest versions here, and I'll just push them up.

@Matthew Kerns [52:35]: Yup Sounds good. Yeah. I'm definitely, yeah, I think I I will, I wanna map out, make sure I understand the lay of the land. And get At least, I think getting an SOP on

@Matthew Kerns [52:54]: Just how it Can be used currently is gonna be probably the thing I start with.

@Trent [53:01]: OK.

@Matthew Kerns [53:03]: And then from there, it's like I'll just see what, what that gives me, and then I'll go from there.

@Trent [53:12]: OK.

@Matthew Kerns [53:14]: Cause that can help map out requirements and Clean up the tasks after that, but I think that is the most like, OK, I'm gonna start doing by mapping out how they currently can use it.

@Matthew Kerns [53:31]: And should use it, and then

@Trent [53:33]: And then how we're gonna

@Matthew Kerns [53:33]: That might be In itself Yeah, so

@Trent [53:36]: Yeah, yup, I'll give you an idea of what we're working on Yeah.

@Matthew Kerns [53:40]: Yeah

@Trent [53:40]: So But yeah, I'm, so that's what I'm doing right now is I'm just gonna ask it, it's bringing down right now, it's

@Matthew Kerns [53:41]: So

@Trent [53:50]: I'm making sure it's doing what it's supposed to be doing here. Yeah, it's using my plugin, it's going and getting it,

@Matthew Kerns [53:54]: And that

@Trent [54:00]: So. Well Exported, you mean exported. So using the skill, OK, it's using the API, it's getting it, it's exporting it, OK, got it. Yeah, it's saving off the 3 workflows, and then it's gonna commit and push.

@Matthew Kerns [54:19]: OK And then I know at some point, I'm gonna want to standardize and replace the HTTP nodes with the jobber note. I did try and attempt at that last night. I'm not sure if you saw my WhatsApp messages yet, but

@Matthew Kerns [54:37]: I think it's

@Trent [54:37]: Yeah, I saw you saved it to a feature branch or something.

@Matthew Kerns [54:40]: Yeah, I made an attempt at it. I haven't tested that at all, but It's, I think if, if we're running into too many errors and they then workflow. It's gonna make sense to Standardize with a node.

@Matthew Kerns [54:57]: I'm not sure what, at what point that is though. Cause like we wanna make sure that we're just doing and making progress towards the parody. And we don't want to get bogged down, but it might be actually faster to do it that way. So I'll think about that when it gets I come through, but.

@Trent [55:13]: Yep Yeah, I think through that, but I think I'm, yeah, I just Hold on Could not read username. It's just it's not a username or. It's the same Which

@Trent [55:34]: OK, so now it's, it's in the main, main branch right now.

@Matthew Kerns [55:39]: OK, sweet

@Trent [55:41]: All right, so you, you should see a notes in there, I think, We'll commit to that. So.

@Matthew Kerns [55:52]: OK

@Trent [55:52]: Phone number null handling fix. So if you see that Data table node operation fix.

@Matthew Kerns [56:00]: Yup, I see bug fixes and and they then sync commit now.

@Trent [56:04]: Yep. Yep, there you go. So. So it's up there So you can, Do what you gotta do. but

@Matthew Kerns [56:15]: Yeah, thank you, bro

@Trent [56:17]: Yup

@Matthew Kerns [56:17]: Amazing stuff. I feel like I, I slept in the day and now I'm awake and I'm ready to go. make some progress here, so.

@Trent [56:28]: Fantastic All right. Hey, Kelsey texted me. Let me see what he says real quick.

@Matthew Kerns [56:30]: Yeah. OK

@Trent [56:40]: He says, can you record my outbound calls from Quo and send them to Capsule. I mean, a jobber number just like the inbound ones. I just got done working on resket. I'm driving back to Phoenix. I didn't realize it's probably 8 o'clock there, so just hit me up tomorrow, have a nice evening.

@Trent [57:05]: So he wants to know if we can take outbound calls from Quo and send them to capsule.

@Matthew Kerns [57:12]: I wonder why This is, yeah, I mean, Something we should consider, if we should plan into phase one or phase 2. But I'm thinking like feature, this is one of those situations where it's like feature requests might just go straight into the phase two, proposal.

@Trent [57:35]: Yeah, this is, this is a feature request into phase two, in my opinion, yeah.

@Matthew Kerns [57:40]: Yeah

@Trent [57:41]: We didn't even have caps as a, even in our scope at all.

@Matthew Kerns [57:42]: So.

@Trent [57:46]: Other than understanding he had it.

@Matthew Kerns [57:46]: Yeah I'm curious why, because what is, like, why does he want it encapsule? But maybe that's something that should be a conversation between him and Mikhail.

@Trent [57:58]: Yeah It. I mean, he's texting me, but yeah, that's possible. I mean,

@Matthew Kerns [58:09]: Yeah, maybe not right now, but just in terms of the roles and like Client Developer. Like how we want to run things,

@Trent [58:21]: Yeah, how we want to operate, yeah.

@Matthew Kerns [58:24]: Cause we're gonna have to start building for SNS here pretty soon too, so.

@Trent [58:37]: Yeah. I'm gonna, I'm gonna tell him, yes, it's possible, but it's not in our scope currently. we can add it to the wish list. But at the end of the day, I'm curious why, right? Well, I don't know, should I even say it's possible? It's probably don't even see. I'm just gonna ask him why.

@Matthew Kerns [58:51]: Yeah, Yeah, OK, that's good cause I was wondering why, and he's thinking about it now. He'll give us a whole, he'll give us a whole bunch of reasons why, probably.

@Matthew Kerns [59:08]: He's on his drive and he just thought about it. That's a good question. How much longer do you have on this call? Because I wanted to ask, I wanted to touch on Exigent real quick if you have time.

@Trent [59:22]: Yeah, I don't wanna be on here much longer, but if it's just gonna be maybe a, a few minutes I can touch on it, so.

@Matthew Kerns [59:29]: Yeah, OK

@Trent [59:32]: So what do you think on this

@Matthew Kerns [59:32]: Well, just, well, I mean, did you hear, you heard my message earlier. Do you remember? Or should I go over it real quick?

@Trent [59:40]: You were saying that maybe we use Now I'm trying to remember. Just go to recap it for me.

@Matthew Kerns [59:45]: Yeah OK, yeah, I'm just thinking that like So Tim wants an example deliverable from an audit, basically. That is my understanding, right?

@Trent [1:00:01]: Yeah, he wants to know, he says it would go a long way if we could show like the Like the The artifact documents, the deliverable documents, anything that has a visual aspect to it that would go, it would, it would help him sell it internally.

@Trent [1:00:20]: So I gave him, I showed him the screenshots of the three-step framework document, when I was there.

@Matthew Kerns [1:00:20]: Yeah. Mhm

@Trent [1:00:28]: And I told him that what we were expecting to be able to output was Effectively that What we've

@Matthew Kerns [1:00:36]: Yeah

@Trent [1:00:37]: Now know about audit flow, it doesn't Follow that perfectly. Like to an exact, but It does much of it, like a quite a bit of it, but it doesn't do all of it. So my question to us,

@Trent [1:00:55]: Is Do we fill in the gaps Do I do I send him the Images from the three-step framework and let him use that as, hey, look, this is the type of content you can expect to receive, but the visuals will be entirely different.

@Trent [1:01:15]: Or The content's similar but not exact.

@Matthew Kerns [1:01:17]: Yeah.

@Trent [1:01:20]: Right?

@Matthew Kerns [1:01:20]: Cause in the proposal, there's already those visuals of like, this is opportunity matrix, this is a process map. So what I'm thinking is we take it a little bit further, just iterate a little more. And we can either use plotter mechanics.

@Matthew Kerns [1:01:39]: As like This is This is what we've determined so far as like Maybe we put together an ROI calculator, a real Data from things that we've done, ROI calculator, because we have the example one from Morningside as ROI calculator, right? I think that would be the thing that

@Trent [1:02:00]: He, he had the, we have the formulas.

@Matthew Kerns [1:02:02]: Difference.

@Trent [1:02:03]: We have to build it

@Matthew Kerns [1:02:07]: Yes We have an example output. like he's looking for Example output to show the stakeholders of like This is what

@Trent [1:02:19]: What's the value that they're getting, right? They want to understand the value they're getting for $30,000.

@Matthew Kerns [1:02:25]: Yeah And, and we're not promising building anything. We're promising

@Trent [1:02:26]: And Correct

@Matthew Kerns [1:02:30]: Like, we're gonna go through your systems. We're gonna go, we're gonna talk with you. We're gonna get A massive quantities of details so that we can refine these numbers and give you something that's like These, these pieces, if they're built, will give you this ROI with like high confidence.

@Trent [1:02:53]: Yeah, I think that that would be something that they would be super happy to see, right? And there were If we do the audit Or what we call an AI opportunity assessment. If we do that And we can give them a

@Trent [1:03:11]: A document that says, here's the highest impact things with the lowest. Lowest effort, or here's the things that we see as opportunities And here's your expected ROI out of them.

@Matthew Kerns [1:03:24]: Yeah.

@Trent [1:03:24]: How, how we got there in between might be interesting, but that alone is Probably the most interesting piece.

@Matthew Kerns [1:03:35]: Yeah, I think the output is, is that like the, the roadmap, like, OK, all the high impact things and then ranked from like, this is low, low effort. We start with these and then we'll build to like the grand vision. These are the high impact things like this is the ROI we're expecting, and so here's your expected cost for that deliverable.

@Trent [1:03:40]: Yes.

@Matthew Kerns [1:04:01]: I think also, I'm not sure if you saw Denise's latest message. It was like right before we got on this call. So he sent out a proposal for 15,000 that has very much similar,

@Matthew Kerns [1:04:19]: Thing to Exigent like he's saying that the next phase, it's going to be like 40K to 100K, and he's waiting to hear back. I think it would be worth it to potentially meet with him, or at least just share with him what we're doing and

@Matthew Kerns [1:04:35]: And Try and ask him for his proposal and Get some back and forth going there.

@Trent [1:04:43]: Yeah, that's fine. We can get his feedback on it, but I, so I don't want to delay on my response to Tim for some outputs. Like, I didn't have anything to send to him right now, obviously, but I don't want to take another week to respond. So we just need, we need to be quick on this.

@Matthew Kerns [1:05:01]: Yeah, Yeah Yeah. So what's the time frame that you're targeting?

@Trent [1:05:07]: I'd love to have it tomorrow

@Matthew Kerns [1:05:10]: OK

@Trent [1:05:11]: Like I just love, love, like, I mean, We don't have to have the actual deliverables. We just need to have something to show him The expectation, and I feel like at a minimum, we could just take the three-step framework images and put them into a document real quick and send them to him.

@Matthew Kerns [1:05:32]: Yeah. I mean, we didn't, but didn't, wasn't that already in the proposal?

@Trent [1:05:37]: Not in the final proposal, only one image was in the final proposal.

@Matthew Kerns [1:05:41]: Oh. Which image was it Opportune matrix

@Trent [1:05:44]: It was the oppo I think it was the opportunity Matrix, yes. So originally I had many images in there.

@Matthew Kerns [1:05:47]: So

@Trent [1:05:51]: Like all of them

@Matthew Kerns [1:05:53]: Hm, yeah And then it was Nick's feedback that got us to reduce it.

@Trent [1:05:56]: But Yeah, we had some feedback across somewhere. I don't remember exactly what it was, but it was basically to reduce it down to just one. One graphic

@Matthew Kerns [1:06:10]: OK

@Trent [1:06:10]: That was the like the meaningful piece or a meaningful piece, and then we chose the opportunity matrix because It's a, it's easy to understand.

@Matthew Kerns [1:06:21]: Yeah.

@Trent [1:06:22]: Compared to the rest of the graphics. But I think the one with the most value ultimately is either the blueprint, like the plan, the big picture plan, and the ROI Those are like those are like the two pieces that

@Matthew Kerns [1:06:33]: Yeah

@Trent [1:06:36]: Are really

@Matthew Kerns [1:06:38]: Yeah. I, I think it's very likely that we just add those two graphics and see what he says like by tomorrow because like speed. And those are things like Now that he's seen that one, it's like, OK, yeah, but we need more detail. And then this is how we can provide more detail. And then if we can do that quickly, then he has the opportunity to ask for even more detail if he wants, right?

@Trent [1:07:06]: Yeah Yep, he does. He has the opportunity to do that. He said that early next week, he's going to be at a convention, so he's gonna be at a

@Matthew Kerns [1:07:13]: OK.

@Trent [1:07:15]: And he, he'll be back in the office between Thursday and Friday or on Thursday and Friday.

@Matthew Kerns [1:07:20]: So

@Trent [1:07:20]: So he wants me to sche he wants to schedule a follow-up meeting for Thursday or Friday.

@Matthew Kerns [1:07:25]: Yeah, so I fully Agree that like quickness here is Important, especially because we have quality things that we could follow up on, like, Like maybe even tonight, shoot over those two graphics and say,

@Matthew Kerns [1:07:43]: We can We can show you A full exam or like we can show you Poten like, maybe not even promise anything yet, maybe just shoot him over those quickly so that he can take a look tomorrow.

@Matthew Kerns [1:08:02]: What do you think of that

@Trent [1:08:02]: Yeah. I mean, I could shoot him over, I could try to shoot him over tonight. I would like to put them into a I mean, I actually have the original proposal to add all the images in it, I could, trim out the content or something and just have titles on them.

@Trent [1:08:20]: Like as a an addendum Or like a

@Matthew Kerns [1:08:24]: Yeah, I like

@Trent [1:08:24]: You know, an addition, an addition to the proposal.

@Matthew Kerns [1:08:29]: Yeah, just add like an addendum to the proposal and and send that over.

@Trent [1:08:34]: Yeah.

@Matthew Kerns [1:08:34]: Well, I'll leave it to you whether you can I mean, unless if you want me to, to do that tonight and then just kind of Cause I know you gotta get off, and I can send it to you, so that you can wake up to it tonight. I mean, in the morning, or I can shoot it to you just whenever I have it done. If you wanna do that or

@Matthew Kerns [1:09:03]: What do you think

@Trent [1:09:05]: I think if you just wanna focus on plotter, for now, I think that I can probably hammer that out pretty quick in the morning. So I'll just, I'll do it first thing in the morning when I get up.

@Matthew Kerns [1:09:12]: OK.

@Trent [1:09:15]: And then, and then, you know, when he gets in the office, he'll have it.

@Matthew Kerns [1:09:15]: OK OK, nice. Yeah, that's the important thing. OK. Sounds good.

@Trent [1:09:24]: Yup, yup. So, shouldn't be a problem. I don't think it'll be a problem for me to do. I have the document. I really just need to trim it down to where it's, you know, an addendum to the proposal.

@Matthew Kerns [1:09:33]: Cool. Yeah, let's do that. I think that's a really good plan, cause it'll be like just quick. He gets to see more of the deliverables and then we can, we can still like do more detail for that follow-up meeting.

@Trent [1:09:51]: Exactly, yeah, anything that we can provide, you know, going forward for the follow-up meeting on Thursday, Friday, that would be, that would be good. So, but he, he's trying to sell it to his internal, like his, you know, his co-workers, the stakeholders within the the business. They're the ones that all have to make the decision on whether or not they spend $30,000 on us.

@Matthew Kerns [1:09:59]: Yeah. Yeah. So I'm also thinking that it it might be useful just if I, me or you updates the DIY pod and tells them the situation, or at least tell Denis the situation, and then we can potentially

@Matthew Kerns [1:10:30]: Add to our level of detail by just going over it with him if he, I mean, he might think it's a good exchange of value, so he might prioritize it, like, so we can do that before, like, long before the next meeting with Exgen.

@Trent [1:10:44]: Yeah, yeah Yep, we can do that I think that's a good idea. We can reach out to me if you want to, you can just hit him up, and you'll see if he's interested in Having a chat, I don't know if I have a lot of time tomorrow to do that, but if we do do it tomorrow, it would be best for me in the afternoon, Eastern time.

@Matthew Kerns [1:10:58]: All right, well, OK. Sounds good. I don't wanna keep you too much longer than we've been on for a while, but

@Trent [1:11:11]: But. Yeah, I'm ready to hop off, but if there's anything else, you know, just message me. I'll probably be awake at least for the next probably for the next 2 hours, but So if you need it, just message me.

@Matthew Kerns [1:11:23]: OK

@Trent [1:11:26]: OK?

@Matthew Kerns [1:11:26]: All righty Sounds good

@Trent [1:11:27]: All right.

@Matthew Kerns [1:11:28]: Thank you, sir.

@Trent [1:11:28]: Cool. Yup, thanks. See ya

@Matthew Kerns [1:11:31]: All right. See ya

