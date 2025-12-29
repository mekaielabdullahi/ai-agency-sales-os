# Meeting Transcript - December 22, 2025

**Meeting:** Plotter Mechanix Onboarding
**Date:** 2025-12-22
**Attendees:** [TBD]

---

## Transcript

@Trent [0:27]: If you're talking, Matthew, I can't hear you. Give me a second.

@Matthew Kerns [0:32]: OK, I'm gonna try and rejoin Can you hear me now

@Trent [0:44]: It might be me. Hold on

@Matthew Kerns [0:46]: OK

@Trent [0:49]: Might be my headphones

@Matthew Kerns [0:51]: OK. let me know if you can hear me. I'm gonna try and keep testing, testing, testing. Good yet

@Trent [1:04]: Test test, can you hear me

@Matthew Kerns [1:06]: Yeah, I can hear you

@Trent [1:08]: Yeah, I can't hear you. That's All bored

@Matthew Kerns [1:10]: Yeah OK

@Trent [1:17]: I don't know why they were working on the Hall we were just on, but not this one.

@Matthew Kerns [1:22]: That's weird. My, now you can hear me though

@Trent [1:26]: Yeah, I got you

@Matthew Kerns [1:27]: OK. Cool

@Trent [1:29]: OK So here's my

@Matthew Kerns [1:31]: Yeah, that's a lot of Yeah, go ahead, go ahead

@Trent [1:33]: Yeah, I was gonna say, here's my initial thought, you know, he just rambled on giving us a bunch of gold. And while we were not being responsive, like verbally, we weren't responding, right? But That's cause we both realized that by him just going on and on about that, that we could just pull that stuff out and that's, that's value, that's gold right there, so.

@Matthew Kerns [1:53]: Yeah, yeah, exactly The more we let talk, the more we get the.

@Trent [1:55]: So Yeah Exactly. I mean, we can sit there and talk all day long, but it doesn't really help solve his problems, you know, if we, if we have his time, we need him to talk as much as possible. He didn't have a problem doing that.

@Matthew Kerns [2:08]: Yeah. Yeah, exactly Yeah, I mean Now, but now we can kind of talk about, I guess, like a recap or what initial thoughts maybe before we process. This stuff But I think it's just like, there's so much volume of

@Matthew Kerns [2:30]: Of communication, and it all just needs to get into Joer somehow, like, details about client work and, and job activities and stuff. just all need to get into Joer, so.

@Trent [2:47]: And then how does that, but then how does that get surfaced for him in an organized way? Is it because they're not using jober effectively, or is it because, like, is he overwhelmed because there's too much stuff?

@Matthew Kerns [2:47]: Actually

@Trent [3:01]: Is it because he doesn't feel like Jaber is the only source, so he has to go get text messages, and he has to go get emails as well. Like what can we do?

@Matthew Kerns [3:10]: Yeah

@Trent [3:12]: To try to bring all that together so that it's less overwhelming for him, right?

@Matthew Kerns [3:17]: Yeah, I think, he wants to use Jabber as the primary source. Like he kept saying like, OK, I wanna, like I look at Jaber for to figure out like where am I going today, right? So he At least that stuff is there cause that's probably the most important thing that like Alyssa makes sure is updated before the day starts, she's like, got it where it's, it's in place, but he needs, I think he needs a combination of AI and ALISA

@Matthew Kerns [3:46]: To be just like

@Trent [3:48]: Grabbing things and doing things with it

@Matthew Kerns [3:50]: Yeah, like managing the communications, getting everything organized into a job or so that he can just speak to something and things will get updated by a combination of AI and Alyssa, and like it's too much for Alyssa to do, so we need to like set up the AI automation to to handle a lot of processing and then just surface to elicit things that like maybe she needs to review.

@Trent [4:19]: I think right now we need to always have a plan to provide feedback on what the AI has done, right? What are automation has done. Something, whether it be a summary or just, I think we need to have that For a couple of reasons. One, it gives them confidence that something is happening, right? And then the second thing, oh, and they feel like they're included, right, in, in the process.

@Matthew Kerns [4:40]: Mhm.

@Trent [4:46]: And then also to capture anything that might go awry. Anything that's not quite happening the way that it should be, right?

@Matthew Kerns [4:55]: Yup. So. Maybe we even start with that. Like we just start with reading everything, and then we put together like a summary of like updates we would make, and then we kind of can run that by them or, or at first we'll just be reviewing it ourselves.

@Trent [5:14]: I'm, I'm kind of wondering I'm kind of wondering if we could leverage The API To just pull a bunch of stuff.

@Matthew Kerns [5:26]: Mhm.

@Trent [5:27]: Store it in a database or something just so that we have Act like More rapid access to it, not hitting the API all the time. To do an evaluation of what the data looks like and how it's being used.

@Matthew Kerns [5:36]: Yeah Yeah, I agree. I think that would be useful. And like set up a maybe air table or something and just pull in Get all the clients,

@Trent [5:51]: I was just thinking, yeah, I mean, I was thinking post grass. But we can do air table, air table, the problem I had with AirTable was the API felt slow.

@Matthew Kerns [6:01]: OK

@Trent [6:02]: Like for large amounts of data, I didn't feel like it was gonna work out well.

@Matthew Kerns [6:09]: OK. Yeah, whatever, I mean, whatever, if you feel like post stress would be better. We can start there. For sure

@Trent [6:16]: I think that scale it is. I think like when we're working through large amounts of data, I think it's gonna be better to try to put it maybe in post press.

@Matthew Kerns [6:24]: Yeah, I guess the question is like how large does the data need to be for that?

@Trent [6:30]: I don't know. Is there anything you can do with the API to just maybe get a count on some things, like how many quotes, how many jobs, how many visits. I don't know what the API allows, but instead of going in and like retrieving all of it and then counting it. Is there just a way that we can say, well, what's the count on this?

@Matthew Kerns [6:51]: Yeah. Yeah, I mean, we can also just look at So their clients, I think there's a number Of clients. There's 1570 results under the clients right now, and then Requests, there's a 136, like just looking at the jobber dashboard.

@Trent [7:09]: Mhm All quotes I36 results, and that's filtered.

@Matthew Kerns [7:13]: So $500

@Trent [7:17]: But it's filled by status all calendar all salesperson all. So that's everything but Everything since

@Matthew Kerns [7:34]: Like August last year

@Trent [7:57]: I mean I've got October of 24, August of 24, yeah, it's the last. August 13th of 24 is the last. Quote that we have in here. And then

@Matthew Kerns [8:12]: OK.

@Trent [8:13]: Jobs, it's good jobs. Jobs is where he actually has a large amount of information inside of. All of the jobs. He's got 1,562 jobs.

@Matthew Kerns [8:26]: Mhm

@Trent [8:28]: Let's look at the requests. He's getting requests

@Matthew Kerns [8:31]: In the jobs

@Trent [8:33]: Good

@Matthew Kerns [8:33]: Jobs in the future also. I think he, I think he said they don't use requests that much.

@Trent [8:42]: Because he didn't like the form or something. It's like a user form, like, I'm guessing a front facing client form that they fill out information to December 12 and upcoming, the before December 12th, so this

@Matthew Kerns [8:54]: Yeah

@Trent [9:02]: Like, there wasn't anything since August of 24.

@Matthew Kerns [9:06]: Mhm So they don't use it hardly at all.

@Trent [9:10]: Give me a second, Matthew, I'm gonna answer this call. For some reason they keep calling.

@Matthew Kerns [9:15]: No worries

@Trent [9:52]: Like Get all these like Spam calls For like property calls. They're, I got I've got a house that I used to own. Sometimes I get calls on that still, even though I don't own them anymore. It calls in this house. I have a piece of property that's next to my mom's property. It just has my name on it. I didn't buy it. My mom put the name on it. So I get phone calls for that property. It's like, I don't know what's happening, but I just get phone calls about, hey, we would really like to give you an offer

@Trent [10:25]: All the time

@Matthew Kerns [10:25]: Yeah I get, I get spam calls all day long, and I don't even answer my phone anymore. I literally just, it's so bad, it's probably like, I should, it's probably calls that I'm missing that are important, but I, I just kinda let things go to voicemail, and then like

@Trent [10:43]: I usually do too

@Matthew Kerns [10:44]: Yeah

@Trent [10:44]: I usually do But this number has called me a couple times. And I'm like Maybe if I answer it and just tell him I'm not interested, they'll take me off the list or something because they keep calling.

@Matthew Kerns [10:58]: Yeah Yeah. I don't know how, I wonder how Kelsey does that cause it's like He can't not answer calls, like he has to answer every single one, and so I bought a bunch of them are bullshit, but a bunch of them are Requests for the business, but they're just such small things, that those are the things that I think we can get automated away somehow, like.

@Trent [11:16]: Yep We can handle some of those, right? I mean, if it's a contact that we know of, then we should be able to route it somewhere. If it's not a contact that we know, then there might be like a screening step somehow. I don't know if they can get a caller ID. I don't know if the caller ID comes in so you can get an idea of who it is.

@Matthew Kerns [11:28]: Mhm

@Trent [11:41]: Potential spam flags, you know how you get it on your phone, you get like a potential spam. I don't know if you can get that through quo.

@Matthew Kerns [11:41]: Mhm

@Trent [11:49]: I mean, I don't know

@Matthew Kerns [11:51]: Yeah, and then Based on whatever they say, so maybe there's like

@Trent [11:54]: What

@Matthew Kerns [11:56]: What I'm thinking is a voice agent. That we set up, and I saw that Jouber has A way to set up a voice agent within Jobber, and they, but they charged $99 a month.

@Trent [12:10]: Who

@Matthew Kerns [12:10]: But Yeah It's like a receptionist, there's like a tab on there that says receptionist. I don't, that might be an option though.

@Trent [12:21]: Yeah, I mean, we have that with quo though too, so

@Matthew Kerns [12:25]: Yeah

@Trent [12:26]: I'm kind of wondering about how they've got a phone number in Jobber and a phone number in Vonage. A phone number in Kelsey's phone.

@Matthew Kerns [12:33]: Mhm

@Trent [12:35]: So They don't, it sounds like they don't tend to call Alyssa directly that much. It sounds like maybe some do, but not many. I don't think that's, that's kind of an edge case. I think most of this is Kelsey's phone. And the business, or maybe the job or phone number.

@Matthew Kerns [12:56]: Yeah

@Trent [12:56]: Like I mean I'm not sure what the story is on the job or phone number.

@Matthew Kerns [13:03]: Same Cause Kelsey, but Kelsey wants to talk to customers But

@Trent [13:10]: Yeah, he does. But what we need to do is filter out the noise.

@Matthew Kerns [13:14]: Yeah, exactly

@Trent [13:16]: We need to get him the things that are high priority for Kelsey. To talk to them about. So, how do we

@Matthew Kerns [13:21]: Yeah.

@Trent [13:25]: I mean, they're paying $379 a month. For Jobber

@Matthew Kerns [13:33]: OK Hm. Yeah, it's like how do I identify the noise, and I think I mean, once stuff is going through quo

@Matthew Kerns [13:53]: We can kind of look at the conversations and just be like, oh This was like a I think eventually we're gonna have like a an SOP or FAQ That's just like, do you guys do this? Do you guys do that? And You know, that'll filter out a good amount.

@Matthew Kerns [14:12]: So there's some high leverage stuff there that's like just from having a voice agent that answers like a few basic questions. That can help us filter out a bunch of noise. The only question is where, where does that live?

@Trent [14:26]: And then is there anything, any event or any criteria for bypassing that. You know what I mean? Like, if it's a contact that we know of.

@Matthew Kerns [14:36]: Mhm

@Trent [14:36]: Is that, is that criteria enough to go around the digital receptionist?

@Matthew Kerns [14:42]: I don't think so because I think he still gets calls from clients that are noise, that are like Do you guys, do you, like, he mentioned something like, do you guys sell paper?

@Trent [14:54]: Right, he doesn't want to deal with the paper situation. He would prefer that that just gets handled in the back end. Like he doesn't care that much to talk to somebody about making sure he gets his paper, but if it has some other opportunity tied to it, like, hey,

@Matthew Kerns [15:09]: Yeah.

@Trent [15:10]: Something is mentioned on the call that he can potentially upsell them to a new printer, right?

@Matthew Kerns [15:17]: Yeah, it's like, there's gonna be high income topics, and then there's gonna be low income topics, and we can filter and be like, OK, what is this person want? And then if they, if they want something that's like

@Matthew Kerns [15:33]: If they're calling to talk about something and the AI is like, OK, this is potentially a high income conversation, then right away we can set up where it just says like, we're gonna redirect you to Kelsey like right now.

@Trent [15:47]: Yeah, yeah, and then, What do we do at first? Do we try to get quo in the middle and evaluate all of the Text messages and all the phone calls and use that to help us make decisions on routing, like, don't do any routing at first.

@Trent [16:12]: And just let the messages pass through and see what we get. Or are there things that we know need to be fielded.

@Matthew Kerns [16:16]: Yeah I think We gotta do Both sides, so we gotta start Analyzing all the communications we can, like let's get all that set up where we can

@Matthew Kerns [16:34]: We can analyze all the communications. Get it all like into a database, right? And then We need to start identifying like, OK, how, how can we make sure that Joer Is updated

@Matthew Kerns [16:52]: Like, like Kelsey can, how can we get it to where Kelsey can trust Jouber as a source of truth, like

@Trent [16:59]: Yeah

@Matthew Kerns [17:00]: Each, each day, at the end of each day, it's updated or like However that works. I don't know if we're gonna be doing something once a day or just as Like, like right away trig on triggers like as things come in. But

@Trent [17:15]: It's There's definitely gonna be That's gonna be a use case, right? What's the purpose behind the thing? So if you're just getting a daily digest of all the things that happened, then that can happen on a time trigger, but There's, if we get a phone call And it, we somehow get a, you know, let's say it gets fielded.

@Trent [17:35]: And we get like a transcript somehow, and it has information on, you know, he, they want to quote Well, we would probably want to do that right away. We don't want to wait till the end of the day to give them

@Matthew Kerns [17:45]: I Right

@Trent [17:51]: That there's a quote that needs to be submitted, right?

@Matthew Kerns [17:54]: Yeah, yeah. That's probably what he was saying too, it's like, This stuff, like, we can't Have like 2 days go by before, like I asked someone to get it done, and then like 2 days went by, or the weekend went by, and like it didn't get done yet.

@Trent [18:09]: Yeah, he needs a way that we can make sure that it gets done. So So

@Matthew Kerns [18:14]: Yeah.

@Trent [18:15]: We gotta remember

@Matthew Kerns [18:15]: Did you see the

@Trent [18:17]: We gotta remember our primary mission, sorry, our OK, we have to find a way to meet our minimum requirements of what we want to do for the quick win. While providing overwhelming value beyond it. And setting us up the next phase so that he is not even hesitant.

@Matthew Kerns [18:31]: Yep

@Trent [18:36]: To sign for the next. Phase, right

@Matthew Kerns [18:40]: Yeah I think we do need to get a big picture to be like, how do we even

@Trent [18:47]: Tackle the

@Matthew Kerns [18:48]: Does your job or just updating Jabber is like a huge task, like

@Trent [18:52]: That's what I was thinking to do.

@Matthew Kerns [18:55]: Like.

@Trent [18:55]: I was thinking just just jober to get it cleaned up and put it where everything needs to go and getting it in order is a big task.

@Matthew Kerns [19:05]: Yeah, well, I think they have They have a lot of the stuff Fairly organized. Like I know I know he mentioned some stuff about it not being organized, but the, the key thing is making sure it's updated properly, like we don't

@Matthew Kerns [19:22]: We can't update it with Bad information, so we need to Start by just Reading communications and then Understanding the workflow of like, how do things get updated

@Matthew Kerns [19:41]: Where is the time, where, where? Where are things, where the delays happening, like, Cause then So Every day like multiple things come in Right? And Kelsey communicates to Alyssa

@Matthew Kerns [20:00]: Like OK, this needs to get updated for this client, and then she Takes notes on that call, and then she'll go update Jobber. But some of the stuff will get missed and then they'll be back and forth. Like that was a key frustration for them.

@Matthew Kerns [20:17]: So like If we can I mean, o, quo is pretty essential, I would say for that problem.

@Trent [20:26]: I feel like we need to get quo in place like pretty. Quickly, but one of the things I don't fully understand is what does the quo and jober integration that is already It's not in place, but the functionality exists to to tie the two together.

@Trent [20:45]: So I don't know if I fully understand what all that does and how we can leverage that to help us look like heroes.

@Matthew Kerns [20:46]: But Yeah, how does how does that quote OK. I see it

@Matthew Kerns [21:03]: There's an app marketplace in Jabur. And quote, there's a connect button end quote.

@Trent [21:12]: So, should we, before we try to do any of that to their account? Should we

@Matthew Kerns [21:13]: With it

@Trent [21:17]: Try to do it on a developer account?

@Matthew Kerns [21:21]: Yeah

@Trent [21:23]: Because I'm, I'm concerned that what might happen is we might start

@Matthew Kerns [21:23]: I think so

@Trent [21:27]: Testing something and something ends up in the wrong place.

@Matthew Kerns [21:31]: Yeah, exactly Like we can have a just a test quo account, a test jobber. Account, and that's where we do all of our work pretty much. And then like there

@Matthew Kerns [21:49]: We're gonna, well, we're gonna be reading from their jober And reading from their the official quote to get like real data. But yeah, we shouldn't be updating for a while.

@Trent [22:02]: But I'm, I'm wondering when we connect quote a jobber, is there something that it's going to kind of automatically start doing that we don't want it to do.

@Matthew Kerns [22:13]: Yeah, I agree. So we just, we shouldn't connect it yet.

@Trent [22:15]: Like. Up eating like up beating contact interactions or something every time they call and just automatically dumping every phone number into the, the clients list or something. We just want to make sure that we understand what it's doing. Right?

@Matthew Kerns [22:31]: Yup.

@Trent [22:32]: I think my approach to this, if I were just doing this You know, I would, I would be trying to use, we can use the quo that we have that we set up for Kelsey. Use that and connect it to like maybe your developer account, and then just start testing some of this stuff, like, what does it do when we connect the two?

@Trent [22:53]: Without even using N8N or anything, just what did those two do together?

@Matthew Kerns [22:58]: Yeah Cause that might That might do most of what needs to get done, honestly, like, If it delivers on the promises that they say. It's like, I'm looking at this I can share my screen for a sec, but I'm looking at this quote jobber integration, and it's like literally almost everything. It's like

@Trent [23:17]: Yeah I'm looking at it too, yeah Yeah, yeah. So it's saying like I would call summaries and transcripts and ensure your team stays aligned with the and works fast.

@Matthew Kerns [23:21]: Cook

@Trent [23:28]: Sona, your AI voice agent, picks up when your team can't and log it. Each call to Joer, so you never miss a lead. Sink, call summaries with Joer to quickly access context from past conversations. Automatically create a client and request in jobber whenever a new lead calls your quote number.

@Trent [23:49]: Click to call from Joer using your quote number with one tab. So you can reach clients faster without switching apps. I mean, that just that list right there. If we could get all that to kind of function and understand how it functions and describe it in demo it to

@Trent [24:09]: Kelsey I mean That alone Would help alleviate some of these. Concerns

@Matthew Kerns [24:18]: Yeah 100% And then did you see the other The So you saw the Instagram post that I sent the other day about company cam, right?

@Trent [24:33]: Yeah, that, that camera and, and the way he was describing some of his, the way he communicates was, I take notes, I, I might give some verb. I talked to it, right, and I take a picture and then I send it to Alyssa.

@Matthew Kerns [24:34]: The note Yes Yup

@Trent [24:49]: I mean, that's

@Matthew Kerns [24:49]: So So I looked up in the jober at Marketplace, and they have Company cam.

@Trent [24:58]: Oh no kidding

@Matthew Kerns [25:00]: Yeah.

@Trent [25:01]: OK Interesting Well I wonder I wonder

@Matthew Kerns [25:14]: That would be crazy

@Trent [25:14]: I think I think we need to do some, some testing. And plugino and Joer. And Glance at what's happening with Companycam. To see if that's something that we want to bring in earlier, save it and earmark it for later.

@Matthew Kerns [25:28]: Mhm.

@Trent [25:36]: And then we really need to evaluate What Processes First of all Are gonna make the biggest impact. But then, second of all, Are gonna get adopted

@Trent [25:53]: Like We have to try to Relieve them And make it easier on them as well, right? I mean, without trying to overwhelm on change. Change management

@Matthew Kerns [26:07]: Yeah

@Trent [26:09]: We can't throw 100 different, you know, processes at them all at once. So I think if we can simplify what they have to do, And automate as much as possible. I'm hoping that these tools, the way they work together, will help with a lot of that.

@Matthew Kerns [26:28]: Yeah.

@Trent [26:29]: But then we need to explain it to them so they understand how to use it.

@Matthew Kerns [26:34]: Cause like I don't know how o is gonna update the job or Requests and stuff, like is it just gonna dump a whole bunch of information in there that they don't really need, like a giant Summary and transcript, right?

@Trent [26:47]: Yeah That's another thing that we don't know, right? Is that, is it gonna clutter and cause more overwhelm in Jobber. That's what we want to avoid.

@Matthew Kerns [26:59]: Right Yeah

@Trent [27:00]: More more information at this point. Could go the opposite direction on us.

@Matthew Kerns [27:08]: Yeah

@Trent [27:12]: It's like, we need to have it organized and flowing in and a clear manner.

@Matthew Kerns [27:19]: Mhm

@Trent [27:21]: So that it's clear where they need to go for all the things. The nice thing is, is they're already very familiar with Jaber. So if we continue to try to use Jabber as the central Hub here.

@Matthew Kerns [27:34]: Yeah

@Trent [27:36]: It'll help

@Matthew Kerns [27:37]: It might help us if we start using Jabber Like we have a, a test account. We have an account, and we just try and use it for A use case like for our Business, like we try and just map it to agency stuff, like, OK, we're gonna have a discovery call with this new client. Like, what if we started using job.

@Matthew Kerns [28:04]: Actually

@Trent [28:04]: I mean, I'm, I'm not opposed to kind of, I mean, we have to think about at the expense, but I am not opposed to the idea of trying to work through the different scenarios as if we were using it ourselves, then I'm wondering

@Matthew Kerns [28:19]: Is there

@Trent [28:20]: What we should do, what we should do is on this call.

@Matthew Kerns [28:20]: Is there

@Trent [28:24]: Kind of continue what we're doing. And then we should take this transcript. And we should take our Our plan and the transcript we got from Kelsey to earlier today. And try to see if we can come up with suggested scenarios to walk through.

@Matthew Kerns [28:45]: Yup

@Trent [28:47]: A jobber is At monthly how much is

@Matthew Kerns [28:50]: I Yeah, 6 months

@Trent [28:53]: Yeah, they're paying They're, they're doing the teams. If you go to teams. They're doing grow right there, up to 10 users. That's what they're paying for.

@Matthew Kerns [29:05]: OK So we would do connect

@Trent [29:13]: For 170 bucks for a month.

@Matthew Kerns [29:16]: Yeah, that's I mean,

@Trent [29:20]: And that's Well, yeah, that's for 5 users.

@Matthew Kerns [29:27]: What I'm wondering though is how are we even gonna test without affecting their account, without Like,

@Trent [29:35]: Well, what I'm, what I'm saying is, yeah, we gotta use an account.

@Matthew Kerns [29:35]: Signing up

@Trent [29:39]: We have to use a job or account

@Matthew Kerns [29:42]: Mhm

@Trent [29:43]: That's not

@Matthew Kerns [29:44]: What we could do What we could do is The 14 day free trials.

@Trent [29:50]: Yeah.

@Matthew Kerns [29:51]: We could do 2 or 3 of those.

@Trent [29:52]: As long as you can make, as long as they don't have a problem, sometimes they put limitations on the trials. So they don't have an issue with using the API and using the quo integration.

@Matthew Kerns [30:03]: Yeah. That's true I wish they might cause that's

@Trent [30:09]: But I think that if we

@Matthew Kerns [30:09]: Useful

@Trent [30:11]: If we contacted Jobber And told him what we're doing, I think they would help us out.

@Matthew Kerns [30:14]: Mhm OK. Yeah I think so too That's probably the move

@Trent [30:23]: Yeah, so I'm thinking that, you know, should we even do that like right away cause it might take time to get a hold of them.

@Matthew Kerns [30:30]: Yeah, and then with the holidays and stuff, we should probably do that like today.

@Trent [30:34]: Yeah, let me see if I can get a Support phone number or a chat or something. Up like now

@Matthew Kerns [30:44]: OK.

@Trent [30:46]: Prefer where's the support link? Usually, oh, in the question mark, OK. Get support, there's a button for get support.

@Matthew Kerns [31:03]: For the free trial, it says you get full access to all of Jaber's features on the grow plan.

@Trent [31:09]: OK, well, that's helpful. That, that basically gives us what we need for 14 days. Right?

@Matthew Kerns [31:16]: Yeah.

@Trent [31:18]: Do we need it for longer than 14 days? I mean, if you signed up right now, We do need it longer than 14 days because, I mean, I'm going to be gone, you can use it But then I could sign up for another account, so we could

@Matthew Kerns [31:29]: That's not

@Trent [31:30]: We could, we could also do that

@Matthew Kerns [31:32]: Yep, and then Mika could do the last 14 days.

@Trent [31:35]: Yeah, there we go. We have 45 days. And we're not quite 45 days, but

@Matthew Kerns [31:42]: Cause we don't care about losing all of our, all of the information. We just want to like test functionality. So

@Trent [31:49]: Correct.

@Matthew Kerns [31:50]: It'll be fine

@Trent [31:53]: Yeah, I think

@Matthew Kerns [31:53]: But like, I mean, we're using APIs, we don't like we could just on the new account, we could just upload all the information anyways, so. I'm just thinking if we actually try to use it for For a rise group.

@Matthew Kerns [32:09]: Just, I think it would be good just to see How it works for our use case. Like we know our use case. And then

@Trent [32:18]: Yeah

@Matthew Kerns [32:19]: We can see it. Is it too noisy or like how, how it is, and then, yeah, go from there.

@Trent [32:24]: I think our approach right now, we kind of summed it up a little bit that we need to just go ahead and get her own account, link it to quo And start like Going through some scenarios and the way that we can get scenarios and use cases is using the transcripts that we have for this call, previous call, and then maybe

@Trent [32:48]: I don't know what else we have before that, but I know that we'd extracted some stuff that were potential use cases in our, in the plotter mechanics from the OSS.

@Matthew Kerns [32:59]: Yeah

@Trent [33:00]: There's something in there. I don't remember exactly where it was at. That might, that's a little bit of a problem too, but

@Matthew Kerns [33:04]: Well If we think about it, like, I think it's actually, it's like we're a service-based business. Potter Mechanics is a service-based business. It's actually very similar, like there's quotes, there's requests, there's new clients, like, like if we just get Chris hooked up to o. Chris is basically

@Trent [33:17]: Yeah

@Matthew Kerns [33:26]: A lot like Kelsey Cause he's like the one talking with clients initially and getting information and stuff. So it's a very similar use case. So if we just set one up for ourselves and then we like,

@Trent [33:28]: Mhm. Mhm

@Matthew Kerns [33:42]: That'll that'll require us to get Chris hooked up with the outgoing phone calls. So if he calls us from his phone, then that whole meeting gets transcribed, and it can update the the jobber copy of like that client, the new request, like all the discussion we have around quotes

@Matthew Kerns [34:06]: At least over the phone, right? But not everything is gonna be over the phone.

@Trent [34:11]: Correct. That is another for us, that's true for Kelsey.

@Matthew Kerns [34:12]: So

@Trent [34:19]: Most of it is gonna be over the phone. Right? Whether it be, when we say over the phone, we should, we should be clear on Through quo or through Jobber. So I haven't really figured out the job or phone number yet. I kind of am wondering if

@Matthew Kerns [34:34]: Yeah.

@Trent [34:37]: We really would like to have all the communications moved over to quo, so it all funnels in the same way.

@Matthew Kerns [34:43]: Yeah, I think so

@Trent [34:44]: Most ideally,

@Matthew Kerns [34:47]: Yup

@Trent [34:47]: Because he said the phone number in Joer gets redirected to Vonage.

@Matthew Kerns [34:48]: What if OK

@Trent [35:00]: So what all dogs get forward is a vantage.

@Matthew Kerns [35:00]: You have Yeah I haven't even seen any advertisement for a job or phone number. I think they don't, they're probably not even Advertising that

@Trent [35:15]: Yeah, where is it? Cause I don't even see Where that would be

@Matthew Kerns [35:27]: The product. Calm enough.

@Trent [35:34]: So I can answer

@Matthew Kerns [35:38]: Hey Chris Not much, just on a huddle with Trent going over the The pot potter stuff. OK. I think so, yeah

@Matthew Kerns [35:55]: Yeah, yeah, I can do that OK I think he just left probably, Potter.

@Matthew Kerns [36:12]: O for

@Chris Andrade [36:14]: A, what's up guys? Can you guys hear me OK?

@Trent [36:17]: Yeah.

@Matthew Kerns [36:18]: Yep

@Chris Andrade [36:19]: Yeah, I just got a call from SNS And I sent them my login tre. You remember when we were having that issue?

@Trent [36:29]: Yeah

@Chris Andrade [36:30]: And we were, I, I was able to log in through the other login.

@Trent [36:35]: Yeah.

@Chris Andrade [36:36]: If for whatever reason, it, it, it doesn't initiate once, but on the 2nd initiation, it'll do it through Hostinger where I can log in through the admin through WordPress. But then when I go to SS Woolshed.com with the admin to log in through WordPress through

@Chris Andrade [36:57]: The Word WordPress site. It's giving them a critical error in that critical error issue website having a critical error.

@Trent [37:07]: Yeah, it's same issue or new issue?

@Chris Andrade [37:08]: Yeah It's the same one It's the same one, and that he can't even use, I don't know why I'm able to log in. Through Posinger to the Admin portal

@Chris Andrade [37:25]: But when I try to go to the domain itself and log in with the credentials. It gives me this critical issue. So they're still unable to log in and set inventory. So that's going to be something that's going to pop up today during that meeting, at 3. I, I honestly don't know how to assess it

@Trent [37:47]: So right now I'm at the WordPress login screen. I don't know if

@Chris Andrade [38:02]: So I just created a user for like it's He's been charged, please be charged. it has church. So if you I'm sorry, do you have a second to try this?

@Trent [38:20]: Yeah, if you can give it to me, I'll try it.

@Chris Andrade [38:21]: OK. OK So his login is

@Chris Andrade [38:38]: SS Wolfsh sheds. So SS Wolf Sheds with an S.

@Trent [38:47]: Yep.

@Chris Andrade [38:49]: Of OF Williams, W I L L I A M S.

@Trent [38:54]: Yeah Sorry, hold on, hold on I don't have that. This is what the password is.

@Chris Andrade [39:01]: No, this is login

@Trent [39:05]: OK So it's SS Wolfshed at

@Chris Andrade [39:08]: No, no, SS bullshit will of Williams. At gmail

@Matthew Kerns [39:17]: I think like this

@Trent [39:19]: Williams, OK

@Chris Andrade [39:22]: Yeah, at gmail. So SS Wolf sheds.

@Trent [39:27]: Yeah

@Chris Andrade [39:27]: Williams at gmail.com Password Is capital S Wolf. W O R S, Sheds with an S.

@Chris Andrade [39:43]: All ALL D A Y. 2026 No, that's it. No, the only, the only thing should be uppercase is a capital S, that's it.

@Trent [39:58]: OK. S just one S.

@Chris Andrade [40:02]: Yup

@Trent [40:03]: OK, so S Wolf sheds all day. 2026

@Chris Andrade [40:08]: Correct Yeah.

@Matthew Kerns [40:14]: Do you guys think we should switch the huddle to the S&S wolfri.

@Trent [40:19]: Gly we would do that, yeah Yeah, so, yeah, I'm getting a critical error.

@Chris Andrade [40:25]: OK, so it That's it. That's all we wanted to make sure real quick. We're just gonna have to try to talk about it later. I just want to make sure you can get the same thing too, so.

@Trent [40:37]: Yeah, I'm getting the same thing, so.

@Chris Andrade [40:41]: And I can give you guys access to my hosting your account. As well later, later this afternoon if, if need be. So, all right, I'll, I'll let you guys get back to it. I just wanted to let you know that's what's going on with SNS.

@Trent [40:55]: OK, yeah, let's figure that part out. I don't know what's going on there.

@Chris Andrade [40:59]: All right, fellas, I'll talk to you later

@Matthew Kerns [41:00]: OK.

@Trent [41:02]: Yeah.

@Chris Andrade [41:03]: Bye.

@Matthew Kerns [41:03]: Yeah

@Trent [41:07]: Yeah, I don't know

@Matthew Kerns [41:08]: So it's like a login.

@Trent [41:09]: Something happened in the

@Matthew Kerns [41:12]: OK.

@Trent [41:14]: When he migrated it over. This is the WordPress login. So it's the WP dash login.

@Matthew Kerns [41:23]: So is it SS Wolfsheds.com, or is it another site?

@Trent [41:28]: Yeah, if you go to SSwolfsheds.com, you'll get to their main home page and then the forward slash WP login is for administration, for WordPress.

@Matthew Kerns [41:40]: OK. Wait. Sorry, what was it? WP login.php. OK.

@Trent [41:52]: Yeah, I don't, you don't need to do the PHP. It automatically puts that on.

@Matthew Kerns [41:57]: OK.

@Trent [42:00]: But yeah, if you were to go to the root URL, you're just gonna get their web page like a normal person would But the path gets you to the long end and then when you get to the login and you type in the user credentials like I did over on the call, this is what we get. And this is what they were getting for another user as well. It wasn't just this one, it was like somebody else's user.

@Matthew Kerns [42:07]: Yeah.

@Trent [42:19]: And then what Chris found out was that he has a user that he logged in and it worked.

@Matthew Kerns [42:26]: Hello

@Trent [42:27]: So some users are not working and some of them aren't.

@Matthew Kerns [42:28]: Oh.

@Trent [42:30]: Aren't, so

@Matthew Kerns [42:32]: That's a weird one. Yeah

@Trent [42:34]: Yeah, and he's, he's getting crisscrossed between what is Hosting or login versus WordPress login, because hostinger is his account that hosts the Server That runs WordPress.

@Matthew Kerns [42:48]: Mhm.

@Trent [42:51]: And then he has the application, which is run on WordPress.

@Matthew Kerns [42:51]: OK

@Trent [42:54]: That's where the problem is, is the WordPress application.

@Matthew Kerns [43:00]: OK

@Trent [43:02]: The hosted UI So that's

@Matthew Kerns [43:05]: And that's our meeting at 3. So should we try and

@Trent [43:08]: Well, that's, it'll come up. He, it's not what we're meeting at 3 is about, but it's gonna come up.

@Matthew Kerns [43:14]: Yeah OK. Something we can help them with.

@Trent [43:16]: So anyway. Yeah, so anyway Ending SS Wolfsh sheds, moving to Plotter mechanics again. Chris, Chris is a little like all over the place with his communications.

@Matthew Kerns [43:30]: Yeah, I think, well, Maybe I should have asked, like, what is this about? And then

@Trent [43:37]: OK

@Matthew Kerns [43:38]: Yeah, and then we, cause we can end, it's, it's quick and easy for us to end huddles, and it gets automatically the notes, so like, we can, I was even thinking this before like We have these long Long meetings on huddles, but if we actually end them sooner and, and if we can over time just start to identify like new topics of conversation and just end the huddle right at the end of a topic.

@Trent [44:05]: Yeah.

@Matthew Kerns [44:06]: Then Might help just organize

@Trent [44:08]: My love problem is Creating that delineation, like creating that line of We're switching from this topic to the next topic and not coming back to the first topic. So then it gets lost sometimes, well, it's, it's disconnected, it's not lost.

@Matthew Kerns [44:25]: Yeah, yeah

@Trent [44:28]: So, anyway So, Potter mechanics, what is the, like, hottest thing right now. we didn't talk about the A2DP. Stuff. I don't have a clue what to do with that right now.

@Matthew Kerns [44:41]: Yeah. Well, that's text messages. So now, I'm looking at the phone. I think I know what the phone jober number is. It's the built-in receptionist thing. It's like round the clock service by phone or text when you're busy on a job or taking some personal time, the receptionist has you covered. So it's voice calls and text messages.

@Matthew Kerns [45:05]: Schedules jobs, creates work requests, like I kind of think it's possible that we don't even need to sign them up with quote if we have them use this, and they already have a job or a phone number. So I think we just need to consider all the options.

@Trent [45:20]: Yeah, I, I'm with you on that. We should definitely consider all the options that if for any reason, we don't even need quo

@Matthew Kerns [45:20]: But

@Trent [45:28]: We just, we just cancel it, right? There's, there's no damage has been done. So,

@Matthew Kerns [45:29]: Yeah.

@Trent [45:35]: It's easy to undo

@Matthew Kerns [45:38]: Yup

@Trent [45:38]: But, but it says to add it to plan. So how much is it

@Matthew Kerns [45:42]: Yeah I don't know. I don't wanna click that button.

@Trent [45:48]: $99 a month Starting at

@Matthew Kerns [45:51]: OK Yeah

@Trent [46:01]: But he says he has a phone number though. Through Jaber. That's what he said

@Matthew Kerns [46:10]: Yeah. So it doesn't Maybe this receptionist thing is different than just the phone number. I wonder if it's in settings somewhere like. Phone number

@Trent [46:28]: Well, here's a phone number But that phone number OK, here we go. There's a dedicated phone number So let me go to the dedicated phone number. Here's the dedicated phone number

@Trent [46:46]: Right here.

@Matthew Kerns [46:48]: OK

@Trent [46:48]: Your number So, that number Sending texts from the dedicated number is enabled. Receiving texts replies on the dedicated number. So sending and receiving texts, and then phone calls. Phone calls are forwarded to this number here, 606-8845, which is probably his his Vonage number.

@Trent [47:14]: If we were to go back to the company settings, 8845.

@Matthew Kerns [47:15]: Yeah

@Trent [47:19]: Yeah, 884-5 is this phone number right here in the company details. So that must be his, like you go to his website, he's got a phone number on it.

@Matthew Kerns [47:29]: OK I made a dedicated phone number we'll forward to this number. I mean, yeah, ideally he would have one customer facing phone number. Right?

@Trent [47:46]: Most ideally, he would have potentially 2 numbers Like for himself. He'd have a personal number, and he'd have a business number. The business number would filter through the system that we're trying to build him.

@Matthew Kerns [48:00]: Yep And get routed to the appropriate.

@Trent [48:04]: Yeah

@Matthew Kerns [48:04]: Person, receptionist,

@Trent [48:07]: Yeah The personal, I haven't figured out how to handle that yet because he has one number that he basically uses for everything. And I don't know if it's gonna be easy for us to field And route the calls based on whether it's a personal call or not.

@Matthew Kerns [48:26]: Yeah Like he gives out his personal number as the business number for now.

@Trent [48:33]: Right now, what happens is he has a business number. But then almost nobody calls it because they have his cell phone number. And they know that they get a better Or faster response to what they need by calling Kelsey directly.

@Matthew Kerns [48:49]: Yeah

@Trent [48:52]: They don't need his phone number. They need a phone number And we need to field the calls. We just need to route them appropriately.

@Matthew Kerns [49:02]: Yeah

@Trent [49:03]: So the question is, is quo that answer? Or is jobbers Dedicated, sorry, their receptionist, the answer to that.

@Matthew Kerns [49:14]: So we gotta figure out All the Sort of like the process behind that. I think, cause Understanding the What the what the routing is gonna look like and what the process requirements are.

@Matthew Kerns [49:32]: Can help us decide between jober and Quill, most likely.

@Trent [49:37]: OK I keep coming back to that is really that what we need to do is try to develop a plan of what the workflows need to be, right? The workflow for communications.

@Matthew Kerns [49:47]: Yeah It's like the native jober integration Might be really good because then the API Connection is like, like you don't have to worry about that part. The the issue probably is like they don't do AI receptionists as their main thing, so

@Matthew Kerns [50:08]: Are we gonna have all the features that we need. That he needs, which may cause that's what they're supposed to be building it for, but we don't know like how new this thing is, we don't know. The specs, what it actually does.

@Trent [50:23]: So it said

@Matthew Kerns [50:23]: It sounds good

@Trent [50:25]: It sounds good, right? Yeah, it says answers questions and recommends services, keeps up with interruptions and changes to create accurate requests. Books visit for urgent service.

@Matthew Kerns [50:36]: Yeah

@Trent [50:39]: These are like the calls that you can get. Hi there. You've reached Frost and Flame HVAC. Just a heads up, I'm an AI receptionist, and this conversation will be recorded. How can I assist you today? Hi, yeah, I woke up this morning to my air conditioner not working. I have had issues with this air conditioner ever since you guys came and installed it last year. This is absolutely ridiculous. I need it fixed today. Oh, no.

@Trent [51:01]: So, well, I'm really sorry to hear about your air conditioner troubles. That sounds super frustrating. Let's get this sorted out for you. We can book an emergency service to have someone come out as soon as possible. Can I get your first name, please? Did you, were you able to hear that, assume you could.

@Matthew Kerns [51:16]: Yeah

@Trent [51:17]: Yeah.

@Matthew Kerns [51:18]: Yeah

@Trent [51:18]: So Schedule jobs Create work requests Take messages Answer client inquiries.

@Matthew Kerns [51:34]: I was like, what we need

@Trent [51:37]: What I'm concerned about is that a dumbed down version that won't give us the features that we're going to need for our automations that we want to build on the back end. You know what I mean?

@Matthew Kerns [51:50]: Yeah, well, what automations like the Things that we're gonna build later

@Trent [51:59]: Yeah, I guess so

@Matthew Kerns [52:02]: Cause if this This integrates Directly to Joubert and the goal is to update Jobber For now, Like what if this solves the phone side of things, and then we just need to build automations for email

@Trent [52:27]: Can we, one thing we should check is what does the API let us do with these conversations. They get logged, right? It says view transcript and summary. I'm assuming that we have access to get put somewhere, but do we have access to be able to get those because if we can't get those, that would be a limitation.

@Matthew Kerns [52:38]: Mhm. Yeah, it's

@Trent [52:48]: Yep

@Matthew Kerns [52:50]: Very possible that they don't But like there's no, there's no access to New stuff, like that's not in the API in the public API yet.

@Trent [53:01]: Possible, yeah. So if you have the ability to look at that to see what is available in the API relative to this feature.

@Matthew Kerns [53:12]: So I can pull up the specer right now. There's like a So there's a graph QL Sort of like request response. Interface that they expose.

@Trent [53:28]: Yep.

@Matthew Kerns [53:29]: And here's basically the docks, so A whole bunch of stuff What is it, transcript?

@Trent [53:41]: Receptionist is the highest level.

@Matthew Kerns [53:41]: Might be

@Trent [53:46]: Section

@Matthew Kerns [53:49]: Yeah, I don't see it Let's see

@Trent [53:54]: That the try searching the little magnifying glass in the OK, there's client phone filter. What about Lets you escalate calls

@Matthew Kerns [54:08]: These are phones

@Trent [54:12]: And receptionist who drop her website. It lets you add a receptionist to your website. Like a little chatbot

@Matthew Kerns [54:35]: Hm, yeah, I don't know. If we're gonna have access to that. Stuff

@Trent [54:46]: So I'm looking here at Receptionist I'm looking at a dashboard. I clicked on try it out, and then it said, check out the dashboard. So here's the dashboard. It looks like it's, you know, just a demo dashboard.

@Trent [55:05]: Cause you click add to plan, it's gonna, you know, tack it onto their bill. I can click test receptionist, and if I click that, it'll

@Matthew Kerns [55:11]: Mhm

@Mekaiel Abdullahi [55:27]: Are you guys trying to afford the the phonete dropper.

@Trent [55:32]: Actually we're looking at another potential option instead of quo, because we just realized that there is a digital receptionist inside of Jobber.

@Matthew Kerns [55:32]: So we're looking

@Mekaiel Abdullahi [55:44]: Oh, that'll be able to do the routing to pretty much do what Ko was doing.

@Trent [55:48]: Well, yeah, it would in some ways replace what quo, the role of quo. And doing it with less tools. But

@Mekaiel Abdullahi [55:58]: OK

@Trent [56:01]: The nice thing is, is they'd be tightly coupled, right? It's all in the same login and UI that you go in to set it up.

@Mekaiel Abdullahi [56:08]: Mhm

@Trent [56:08]: But The problem might be that we may not have programmatic access to it, may not have an API that lets us get the transcripts, the call transcripts and things.

@Mekaiel Abdullahi [56:20]: Which is kind of what we need it for.

@Trent [56:22]: Which is a kind of a key thing for us to be able to do what we need, we need to do. So we're trying to figure that part out. Learn more about receptionists. Let's see.

@Trent [56:59]: You have to have the plus plan, it can be added to the grow plan, so he could upgrade to the plus plan, or he can add it to the grow plan. Dedicated phone number

@Matthew Kerns [57:16]: Which he already has, I think

@Trent [57:18]: Yeah. Only admin users can get the reception dashboard, OK. Count and billing if you have any questions, blah blah blah. Try your receptionist

@Trent [57:35]: To test it out before you actually choose to add it.

@Trent [57:53]: You know what I mean? Instead of testing it, I would rather know more about its actual details. So manage your receptionist. And do text messaging, answering all text messages to your job or DPN. So that your dedicated phone number, which they have,

@Trent [58:13]: So there it's wanting to know if the AI receptionist can't answer those text messages. Same thing with voice calls. While off, you can still test your AI receptionist by calling your number with the following numbers, OK?

@Trent [58:31]: That's interesting. Secondary number of some sort. Phone greeting Voice, background noise? Do you want to have background noise or not? Answering delay Allow time to ring for 10 seconds before the reception desk answers it.

@Trent [58:52]: Recommended for Google Voice users, OK. Client communications, handle client interactions through your enabled communication channels, information sources, company information, booking and request forms.

@Trent [59:11]: Schedule jobs When enabled for your account, AI reception, it uses your online booking form to schedule jobs into your calendar. The tough thing about having an AI receptionist schedule.

@Trent [59:27]: Jobs Is his calendar has to be up to date. Like everything has to go through the calendar, which I think he said they pretty much do already.

@Matthew Kerns [59:41]: OK Did he say that

@Trent [59:45]: I, I thought he said that if it wasn't in the, if it wasn't scheduled in Jour, then it would get lost or something.

@Matthew Kerns [59:45]: All right. Yeah But like his personal calendar, I don't know, like, How much he updates his digital calendar, cause he hasn't gone on his computer.

@Trent [1:00:05]: Right, availability, like his availability, right? And then the jobs that get dropped in.

@Matthew Kerns [1:00:06]: So

@Trent [1:00:11]: How does it handle the fact that they have Joe versus Kelsey

@Matthew Kerns [1:00:17]: Mhm

@Trent [1:00:17]: Like how do they manage the fact that they can both take calls but they can't take all the calls.

@Matthew Kerns [1:00:27]: Yeah, I Part of me thinks that we need to get as much into Jaber as possible so that they can Just work All using Jobber

@Trent [1:00:40]: Well, I

@Matthew Kerns [1:00:40]: But the

@Trent [1:00:41]: I say we need to come up with the one, we need to come up with the processes, sorry, I'm talking I, there's a delay, right? But, so we need to come up with the use cases or the workflow that we have identified.

@Matthew Kerns [1:00:42]: But Yeah you're good

@Trent [1:00:54]: What we can do, and then get some suggestions, maybe Claude can help us just do the planning of, hey, you should do this, this, this, and walk through it. Right? And then we should try, you already have a job or account you've signed up for.

@Matthew Kerns [1:01:04]: Mhm

@Trent [1:01:09]: Right? Try it inside that job or account because you get everything in the grow, but you don't get the receptionist though, right?

@Matthew Kerns [1:01:11]: Mhm

@Trent [1:01:19]: I think it said you get everything in the grow plan.

@Matthew Kerns [1:01:20]: Yeah Yeah, for the free trial, right?

@Trent [1:01:26]: Yeah, for 14 days

@Matthew Kerns [1:01:26]: So then And then we can test out the the receptionist.

@Trent [1:01:35]: To see what

@Matthew Kerns [1:01:35]: So, Mikhail and another Yeah, another thing we're thinking is Like, we can test out using Jobber For our agency, like, There's clients There's requests, there's quotes, like, we can sort of map our use case to Jobber, and that can get us

@Matthew Kerns [1:01:59]: Understanding On a deeper level, like how we How Useful like these AI. Features inside Jobber are gonna be.

@Mekaiel Abdullahi [1:02:12]: Mhm

@Matthew Kerns [1:02:13]: And the connection to quo and everything, like,

@Mekaiel Abdullahi [1:02:17]: So you're saying we could use strawberry internally to just see if it'd be valuable, For the AI aspect of it, or like the AI tools it offers.

@Matthew Kerns [1:02:29]: Yeah, like mostly for testing, to understand How

@Mekaiel Abdullahi [1:02:35]: Yeah.

@Matthew Kerns [1:02:35]: It works for me, but

@Mekaiel Abdullahi [1:02:37]: Yeah, I can write it up I can like create an account, rout it For number, and then For jobs and stuff, like how would we, and then for quotes and stuff, we could use it to send quotes and stuff as well. I'm looking at my main job right now

@Mekaiel Abdullahi [1:02:57]: But I'm in, so I'm trying to figure out how it

@Matthew Kerns [1:02:57]: Yeah Cause we've started setting up the

@Mekaiel Abdullahi [1:03:01]: Works

@Matthew Kerns [1:03:04]: Like integrations with Jabber, so now I can access like programmatically I can pull client info from Jobber. So if we have like a new account or something, I can just Swap the The authentication, and we can do it for any account, but like,

@Matthew Kerns [1:03:23]: What we can't even do is Take all of our info about clients from our cloud code OSs and just say, hey, let's move all this stuff into Jabber. Create a client for each one, create like Put essentially just upload, create workflows, and upload all of our stuff into Jaber, and then we can

@Matthew Kerns [1:03:44]: Test like Updating that information in Jabber.

@Mekaiel Abdullahi [1:03:50]: To see how it would be use case for Kelsey, right?

@Matthew Kerns [1:03:51]: And we might Yeah And for now, we'll just use trials, but Honestly, if it's working well, like we might end up using Jobber.

@Mekaiel Abdullahi [1:04:02]: I don't, I don't see you or not. Like, if that's something we need to do, like, why not? Like, you just told me to do it, we'll do it, like, you know. Do you guys think it makes sense

@Matthew Kerns [1:04:10]: Yeah.

@Trent [1:04:11]: I think, I think that we're just considering all angles right now, and I think that we need to first understand the value to our, our, our client.

@Mekaiel Abdullahi [1:04:16]: Mhm. And then

@Trent [1:04:21]: And I think through, through experiencing it through the client. You will see the value. So What Matthew, I think his Idea of maybe we'll use it to map it out with our processes and how our business works.

@Trent [1:04:38]: Is that it's a very similar use case, and we can sort of leverage what our model is To do more testing At a minimum We can use our leverage our experience or our Plan

@Mekaiel Abdullahi [1:04:52]: Mhm

@Trent [1:04:53]: To create The workflows To test the workflow

@Mekaiel Abdullahi [1:04:57]: OK. Yeah

@Trent [1:05:02]: So let's see here

@Mekaiel Abdullahi [1:05:04]: The caller hangs up before receptionist can start a conversation. Automatically sends a text message to follow up. That's pretty useful.

@Trent [1:05:12]: So if, yeah, So, I'm gonna say that the feature set is going to be limited on the job or receptionist, but it does have a lot of the basics covered. So it'll field calls, so

@Trent [1:05:29]: It'll answer the call, it'll answer texts if you want it to. You can Have only specific phone numbers. Go to text messaging of the receptionist, if you want.

@Mekaiel Abdullahi [1:05:41]: Mhm

@Trent [1:05:43]: It learns your information about your company, your business profile. Your request booking settings for request forms as a request form and online booking settings. So you can enable those information sources.

@Trent [1:06:00]: So it can work with that. If they hang up On the phone, they call the number and they don't like the receptionist or they didn't like the conversation or whatever. They're partway through the greeting.

@Trent [1:06:19]: It can send them a text message as a follow-up. To enable SMS send back, turn on the toggle.

@Matthew Kerns [1:06:33]: So many of these features are like tiny little things that

@Trent [1:06:33]: That's not

@Matthew Kerns [1:06:38]: If we don't use them, we're gonna need to build ourselves. Most likely.

@Trent [1:06:41]: Well, I mean, maybe, but Quo has a lot of this stuff built into it. But What I'm saying is that Quo has all the things we're showing now. It's But then some

@Matthew Kerns [1:06:56]: Oh OK And potentially less expensive.

@Trent [1:07:04]: Potentially, yeah Well About the same It depends on how many, I think it was depending on how many users they had. Of quo It was user-based

@Matthew Kerns [1:07:17]: OK. Yeah, it's probably the same, similar with droper though.

@Trent [1:07:21]: Jouber said, you know, starting from $100 so I don't know what that means.

@Matthew Kerns [1:07:27]: Yeah

@Trent [1:07:30]: OK, so text back messages are only sent to new callers, people who haven't had matching client profile in the jobber account. Callers who haven't received a text back in the past 24 hours. Callers who haven't replied with stop.

@Trent [1:07:51]: So This is where we're limited in our automations. Like, these are the this is the way it works, right? There's no You turn it on You turn it off, and this is the way it works. There's no anything in between.

@Matthew Kerns [1:08:10]: No customization

@Trent [1:08:12]: Not really, no. You get toggle things on and off, but this text message, this texting back, it just has criteria, conditions inside of it. And it's gonna do the text back if you have the feature turned on. To these callers

@Matthew Kerns [1:08:29]: Yeah

@Trent [1:08:33]: Disabled receptionists for select client conversations. So The receptionist can be disabled for individual client conversations in the message center.

@Trent [1:08:53]: So if you have a known client You can toggle it off, so you can always talk to them directly in the AI agent, the receptionist doesn't reply at all.

@Matthew Kerns [1:09:05]: Mhm

@Mekaiel Abdullahi [1:09:22]: Your phone reading

@Trent [1:09:30]: OK, so there's a routing So let's see what it says Phone greeting Interactive voice response.

@Trent [1:09:48]: When enabled, and let your callers select a number on the dial pad for certain actions, like one to book a service.

@Mekaiel Abdullahi [1:09:57]: So like what he was talking about How

@Trent [1:10:01]: Yep.

@Mekaiel Abdullahi [1:10:01]: Azar me on this country

@Trent [1:10:03]: Yeah, so you can do the phone tree, right? Press one to book a service, press 2 to get started on an estimate. Or leave a message Or speak with someone

@Mekaiel Abdullahi [1:10:16]: That could be like a Go to Kelsey Directly

@Trent [1:10:21]: Speak with someone, you must have escalation policies set up for transfer calls in order to enable this option.

@Mekaiel Abdullahi [1:10:30]: This is in Jaber itself, right?

@Trent [1:10:33]: Yeah. Now, I don't know how far you can customize this. Right? So if there's another item that we would like to have, that we would like to have in our menu

@Mekaiel Abdullahi [1:10:45]: Yeah.

@Trent [1:10:45]: I don't know what else we get options for. It looks like to me we might only be limited to what they put in this menu here.

@Mekaiel Abdullahi [1:10:51]: Yeah. And originally, isn't that why we were kind of using o because it was more Of a tool set And then just use Jabber for like the functionality aspect of it.

@Trent [1:10:57]: It's Yeah, well, so there's a, we'll come back to that in just a second, but Actually, I'll just show it off here. Review real quick.

@Trent [1:11:19]: If you sign up for quo, you get 20% off your 1st 6 months.

@Mekaiel Abdullahi [1:11:25]: Nice, so we should have

@Matthew Kerns [1:11:29]: Yeah

@Mekaiel Abdullahi [1:11:30]: Tell them to cancel

@Matthew Kerns [1:11:32]: Hm Then we got to get the API again. API key

@Mekaiel Abdullahi [1:11:40]: Order your number for free

@Trent [1:11:43]: I wonder if I wonder if we can get the, get it applied. After

@Mekaiel Abdullahi [1:11:49]: Yeah, I'm sure if you reach out to us support though. Cause they should hopefully

@Trent [1:11:55]: It doesn't really show like a code or something, that's what I was gonna try to see if I could find. Partner key Yeah, there's a partner key. So this These things here are what identify.

@Trent [1:12:14]: The offer And where it came from

@Matthew Kerns [1:12:16]: Mhm

@Trent [1:12:19]: But going back to that real quick. Here's the benefits that you generally get with quo. Call summaries and transcripts

@Mekaiel Abdullahi [1:12:33]: It's kind of like big one

@Trent [1:12:35]: Sona Will pick up when your team can't, log each call a jobber so you never miss a lead or a customer. Sync call summaries with Jouber to quickly access context from past conversations. Automatically create client and request.

@Trent [1:12:53]: In job or whenever a new league calls. So it'll automatically add the client and it'll automatically submit a request in Jobber.

@Mekaiel Abdullahi [1:13:03]: Which will solve a lot of his quote problems too.

@Trent [1:13:06]: Yeah. Click to call from Jobber, so Inside Joer there's a button you can click to call and it will link to your quote number so when you When you're talking to somebody in Jobber and you want to call that person, you just touch the button and it calls them from your quote number.

@Trent [1:13:35]: Let's look at this real quick, these pictures. I'm just trying to remind or refresh myself on what quo does. For Joer, right? So Here's all of our Get your business number and start calling in minutes, OK? Click to call from Joer using quote number

@Trent [1:13:53]: So this is inside of Jobber on the left You touch the number and it'll start calling with quo. Automatically create communication records from phone calls made in quo. On the right is Jouber.

@Trent [1:14:12]: So that is a request for New call Test request, it says. And a summary from Quo Then there's internal notes

@Trent [1:14:29]: OK. A sync AI call summaries and transcripts with jober requests. So attached to the internal notes. If we go back here Down here at the bottom Of this request.

@Trent [1:14:46]: This is a request

@Mekaiel Abdullahi [1:14:46]: Yeah.

@Trent [1:14:48]: Internal notes

@Mekaiel Abdullahi [1:14:50]: I'll link it up.

@Trent [1:14:50]: Is Attached the transcript, the call transcript.

@Mekaiel Abdullahi [1:14:55]: Right

@Matthew Kerns [1:14:55]: This is in Jaber, so that's the notes that they, that's like what Alyssa would update, so it's like. Pretty key does does Jaber have that?

@Trent [1:15:05]: Let's go back to that in just a second. OK, I, this is circling background, so it's a carousel. So let me go back.

@Matthew Kerns [1:15:06]: Job

@Trent [1:15:16]: Call, call forwarding. Let me get this real quick. So let's just remember what we were looking at and I just don't want to lose my place. So If you already have a business number, their business number is the jobber number, so that's not really

@Trent [1:15:33]: No, actually it's Vonage. Their business number is Vonage. So you can forward that number to Joer if you want. So the receptionist can pick it up. Set up call forwarding with your forwarding Provider set up call forwarding from Google Voice settings to update in Google Voice, OK.

@Trent [1:15:55]: Update and Jabber. Escalation policy. You can create an escalation policy to ensure that urgent or sensitive calls are redirected to a team member when specific terms or phrases are mentioned. So if they say talk to a person or a leaking water or emergency.

@Trent [1:16:16]: Then it'll escalate It can send a text message notification or transfer the call to The contact listed in the escalation policy.

@Trent [1:16:32]: So The option selected in this example is transfer call, and then they have a Person In the business that it it contacts. And a phone number to contact them at.

@Trent [1:16:49]: OK, so Be routing, what's this? For example, emergencies, speak to manager or urgent. Those are terms that they can use when they're talking to the receptionist.

@Trent [1:17:12]: Notification will be sent to the escalation contact with the transcript snippet, so that's kind of cool. So if you escalate, instead of transferring the call, it'll just send a text message with a transcript snippet.

@Matthew Kerns [1:17:26]: Snippet is good

@Trent [1:17:29]: Transfer the call Immediately transferred to your escalation contact number. But it doesn't have a transcript, right? So. You can add multiple trigger terms to match the kinds of situations your team wants to be notified about. Receptionists will listen to these call.

@Trent [1:17:49]: Or these during calls and automatically initiate your selected escalation method. OK, so here's More of the things we were talking about for Alyssa on the back end, right? A signed follow-up tasks when a receptionist takes a message, it creates a task in your job or schedule to follow up with the customer.

@Trent [1:18:13]: By default, these tasks are assigned to all admin users, however, an individual team member or group member. Can be assigned to the task created by your receptionist. To manage your receptionist tasks assigned, like go to the receptionist dashboard and select the manage tab. Actions assigned to

@Trent [1:18:31]: So you can do task assignment. Create follow up a tasks. When there's a follow-up required, it'll assign a task. If your customer calls or texts your receptionist and isn't ready to schedule a job or submit a request, the receptionist will take a task

@Trent [1:18:51]: In the calendar or create a task in the calendar for you to follow up. From the task details on the schedule. Select view receptionist activity to summaryize this. To see the summary of this conversation So that's pretty good

@Mekaiel Abdullahi [1:19:09]: Nice and simple

@Trent [1:19:09]: Automatically puts Puts the follow-up task in there, right?

@Mekaiel Abdullahi [1:19:13]: Mhm

@Trent [1:19:15]: And it says only if Says by default OK

@Matthew Kerns [1:19:29]: And we do like routing of the follow-up to a specific person for a specific kind of follow-up.

@Trent [1:19:37]: Well, it looks like Assigned to, and then there's a list of people in this little box here.

@Matthew Kerns [1:19:45]: Yeah.

@Trent [1:19:45]: I don't know, I don't know how you route it. But

@Mekaiel Abdullahi [1:19:50]: I'm sure it would pull from like People to assign the task to, right? Or like employees or something, right? Some type of field.

@Trent [1:19:56]: I don't know if it's that, I don't know if it's that advanced. I'm sure it has the users that are part of the company as an option, but you probably need to pick that list.

@Mekaiel Abdullahi [1:20:05]: Yeah.

@Trent [1:20:06]: And it's a static list. It looks like Select manage, task assignment under actions.

@Matthew Kerns [1:20:23]: It could be a process thing or it's just like Someone in the company does follow-ups like Alyssa does most follow-ups, but then Well, as part of the process, we'll identify like, OK, for this thing, like Kelsey needs to be the one.

@Matthew Kerns [1:20:42]: But if it's assigned in jobber, if everything gets assigned to Elissa She can look through and be like, oh, I can't handle this manual assigned to Kelsey.

@Mekaiel Abdullahi [1:20:54]: Makes sense

@Trent [1:20:56]: So there's only one setting. For follow-up tasks.

@Matthew Kerns [1:21:03]: Yeah

@Trent [1:21:04]: When you create a follow-up task, it assigns it to anybody in this list.

@Matthew Kerns [1:21:10]: All of us now

@Trent [1:21:11]: Of the That's it And it will notify the assignees by email if you'd like. But it's everybody in this list, right? So it's not by person.

@Mekaiel Abdullahi [1:21:25]: That sound like Yeah.

@Trent [1:21:31]: So the, the pros here is a lot of the basics are already here The cons are we're gonna be limited to whatever it can do.

@Mekaiel Abdullahi [1:21:39]: Yeah

@Matthew Kerns [1:21:40]: Right.

@Mekaiel Abdullahi [1:21:42]: But it beats developing solutions from scratch, right?

@Trent [1:21:46]: From scratch, sure But I'm wondering Where is that threshold that we need to go over to quo. I think quo gives us the flexibility to build what we want.

@Matthew Kerns [1:21:56]: Look like

@Mekaiel Abdullahi [1:22:00]: On top of Jobber

@Matthew Kerns [1:22:01]: Right.

@Mekaiel Abdullahi [1:22:02]: Well, why don't Or, yeah, I guess cause Quo already has the tools there, and it's just using that on top of. Then, and we can't really change the way we do it, right?

@Matthew Kerns [1:22:16]: I think we could do a hybrid where it's like we use o for some stuff and job or for other stuff, but the only problem is then which phone number is

@Trent [1:22:16]: I mean

@Matthew Kerns [1:22:26]: Like we can do But we can do phone number forwarding, so We can have like one client facing one But it's just, how do we make sure that that all gets wired up. Like if quo is the client facing one. And then it forwards, everything to Jouber.

@Matthew Kerns [1:22:45]: Then we're gonna need to duplicate stuff as well.

@Trent [1:22:50]: Yeah, I, I really like the idea of trying to funnel all the communications through one system.

@Matthew Kerns [1:22:50]: So.

@Trent [1:22:57]: Whether it be job or or quo. I don't know if we want to do both. And then we have to worry about the cost of There's an additional cost to Each tool Right?

@Matthew Kerns [1:23:08]: Right.

@Trent [1:23:10]: So Now, there's not a lot of settings here Is what I'll say, right? And they got the basics in here. They got a lot of really good features. But I mean, what we have is what we have. So we either take what they have and just

@Trent [1:23:28]: Whatever they don't have, we just Deal with it, live with it I don't know. So I see follow-up tasks I see that it will do

@Trent [1:23:47]: Where the, where's the information about what it can do.

@Matthew Kerns [1:23:55]: Yeah, this

@Trent [1:23:57]: I want the transcript real quick. Was it the transcript?

@Matthew Kerns [1:23:57]: OK.

@Trent [1:24:09]: OK, so Inside the receptionist dashboard. You will get the time stamp, a phone number,

@Trent [1:24:25]: Whether it was a call or a text, A summary, just a quick Few words summary Tags There's tags that it will Like general inquiry, job scheduled, things like that. You can click on details of that call.

@Matthew Kerns [1:24:51]: Yeah I didn't see anything about them, like if there's an escalation, then you get A snippet of a transcript, but As far as like logging to a request or like a quote.

@Matthew Kerns [1:25:09]: Based on Well, OK, but the client facing one is the receptionist, right? Internal I think internal operations and communications Like might not be handled by this jober receptionist because it's a client facing receptionist.

@Trent [1:25:33]: Right, this is in intended on being client facing and really only client facing. It's inbound calls, right? You can, you can reply by calling your number or text them from the jobber app or whatever.

@Matthew Kerns [1:25:41]: Mhm

@Trent [1:25:48]: But It's not intended on being internal communications at all. So then we'd have to capture internal communications in a different way.

@Matthew Kerns [1:25:57]: Yeah

@Trent [1:26:00]: I think that that alone is probably Reason enough to say that we probably should just stick with quo. We can use this as a model though. Of what things we should Try to build

@Trent [1:26:16]: If they're not available already.

@Matthew Kerns [1:26:19]: But I'm wondering like Like if maybe it's both, like maybe we end up using both because receptionist, they've already built out so much and Even if there's features missing, it's better than what Kelsey currently has, and they're going to keep iterating on it.

@Matthew Kerns [1:26:40]: Most likely So, if we get them set up with receptionists for the client facing stuff. I don't know if he's ready for the client facing stuff right now though, is the other question. Like maybe we don't start with This.

@Trent [1:26:56]: That's another question. Do we get transcripts At all if we don't use the receptionist? Like when, when Kelsey's making a phone call, do we get communication? Do we get transcript of the call?

@Trent [1:27:14]: Cause I don't know that that's the case here.

@Matthew Kerns [1:27:18]: Right? Like if we don't use, if we don't onboard with receptionists.

@Trent [1:27:23]: Correct I think that the communications that happens between Kelsey and a client is not recorded at all.

@Matthew Kerns [1:27:32]: Yeah

@Trent [1:27:34]: And if that's key to what we're trying to do, that might be A deal breaker

@Matthew Kerns [1:27:48]: Cause if, so if the internal I mean, we wanna get him To start saving time So like He does get a lot of like, just BS calls that come in from Existing clients, potential clients.

@Matthew Kerns [1:28:06]: And if we have receptionists handling that side, then we're just focused on building the internal operations. Then that could be a potential like two-pronged approach where we handle both.

@Matthew Kerns [1:28:24]: And we can get

@Trent [1:28:25]: I just wonder, I just wonder if the com the extra layer of complexity is. There's at some, at some level, it simplifies things, but then at another level, at another stage or point in

@Mekaiel Abdullahi [1:28:40]: OK It kicks the bucket pretty much.

@Trent [1:28:44]: Does What's that

@Mekaiel Abdullahi [1:28:47]: It kicks the bucket because you either have to do it on the front, front end or back end, because I see what you're saying. You just want, you want it coming in from one place, essentially, right? Because I feel like If you, you have to have it come from one place, essentially, like, either quote or jobber. I see what you're saying though.

@Matthew Kerns [1:29:02]: Yeah.

@Trent [1:29:10]: So right now, If someone contacts their phone number through Jabber.

@Mekaiel Abdullahi [1:29:17]: Mhm

@Trent [1:29:17]: It will get routed To Vonage Vonage has a menu system. 1234 Whatever And it gets routed there based on that selection to Kelsey's phone number or Alyssa's phone number or Joe's phone number, whoever

@Trent [1:29:36]: But there's no recording There's not really any fielding of phone calls, meaning what's the topic? What do they need

@Mekaiel Abdullahi [1:29:45]: Yeah Why don't we just forward that number to quote. Like that number that they're using, that goes to Vonage. Why don't we just tie that in the quo?

@Trent [1:29:53]: Yeah.

@Mekaiel Abdullahi [1:29:55]: That way it'll capture everything and then we could sort of

@Trent [1:29:57]: Yeah I, I, I almost, my My thoughts on it really is that we should just stick with quo. And just try to get everything to funnel through quo. So because we have more control in o.

@Mekaiel Abdullahi [1:30:15]: And then we can always feed it back into Jobber if we needed to.

@Trent [1:30:19]: And we get Transcripts for the call, as well as any receptionist.

@Mekaiel Abdullahi [1:30:26]: I agree.

@Trent [1:30:26]: And we can route calls. We can do what Vonage does. And what Joer does

@Mekaiel Abdullahi [1:30:32]: Mhm

@Trent [1:30:33]: If quo But then link it to Jabber so that the information migrates the appropriate information migrates to to Jobber.

@Matthew Kerns [1:30:43]: I'm a bit, I see what you're saying, I think, I don't know Maybe I don't, but With quo, if we have the ability to build more things.

@Matthew Kerns [1:31:03]: Like with more control, we also have to build more. So if there's a bunch of things that are already built With Joer Then I, so I don't see anywhere where we have like internal communications,

@Matthew Kerns [1:31:25]: Handled Like, so we're gonna have to end up building that. But if some things are already being handled. By Like job or receptionist. And then Vonage does routing.

@Matthew Kerns [1:31:43]: Like maybe we use everything that's already built and handling stuff, because also they're gonna add more features So

@Mekaiel Abdullahi [1:31:53]: Down the line

@Matthew Kerns [1:31:54]: Like Like, yeah, so like customizations that we might Be thinking to build, we might build them for a couple months and then all of a sudden on the jobber receptionist like that feature is now available in the next update and, and we some time, so.

@Trent [1:32:08]: Yeah So the only thing I say about that is that I've heard it That don't buy something based on what's promised. Buy something based on what's available today. Because you can't really truly predict what's going to come up, even if they have a roadmap that shows what they plan on doing, which gives you a little insight into their plan.

@Trent [1:32:32]: You should not buy, you should not buy based on what the promise is, but what the, what's available today.

@Matthew Kerns [1:32:33]: Yeah. Yeah, I incentives like wherever like, so quote their only product is this, right? So like,

@Matthew Kerns [1:32:49]: They Their whole success of their company is based on Like all the features that they're like Jobber has a bunch of stuff and they could shift to other priorities away from the receptionists just because somebody else does it better like quote, and then they already have a connection with Quo

@Matthew Kerns [1:33:08]: So. Try and skate to skate to where the puck is gonna be.

@Mekaiel Abdullahi [1:33:18]: I'm sure, it's good to think about You don't wanna waste your time, you know. But it's hard, it's a balance, right? Like, I feel like you could always adapt, right? Something new comes out or if there's another tool somewhere else, but then you don't want to rebuild or like Waste time, I guess, or re-engage or like do something over that you've had to done our do already or waste time like.

@Matthew Kerns [1:33:32]: Yeah Yeah

@Mekaiel Abdullahi [1:33:39]: Once you're doing something and then it's available somewhere else.

@Matthew Kerns [1:33:43]: Yeah, the whole thing is reducing switching costs.

@Mekaiel Abdullahi [1:33:46]: Mhm. So yeah, we do have to think about how we build it.

@Matthew Kerns [1:33:58]: I sort of think that, yeah, like the fastest thing is gonna be whatever is built now, we, we go based off of that and we We might just be wiring up services like at the end of the day we're just wiring things up. Like there's even if we use Jawer, there's gonna be a lot of

@Matthew Kerns [1:34:18]: Configuration on our side like understanding the workflow, understanding how they communicate with clients and making sure that that receptionist Does those things We'll have to do that if we go quo and no jobber also

@Matthew Kerns [1:34:37]: There were just might be more building involved, or I don't know, we still have to look at, yeah, you're looking at the features and stuff right now, so maybe a lot of stuff is also handled by quotes, we have to dig into there and figure out too.

@Trent [1:34:52]: Thea Answers calls, which we expected to be.

@Matthew Kerns [1:34:58]: Mhm

@Trent [1:34:59]: AI message responses. Reply Faster with AI message responses. You also get Can draft a message based on a specific topic or context.

@Mekaiel Abdullahi [1:35:16]: Yeah, I call tags

@Trent [1:35:19]: AI, yeah, we'll get down to that one. And like we're not currently paying for that one, so we'll see. But let's, so contact suggestions. Easily add new contacts with suggestions based on a call and voicemail transcript. I'm not sure what the call context would suggestions.

@Trent [1:35:39]: Suggestions of what Of how

@Mekaiel Abdullahi [1:35:41]: Like maybe a new contact

@Matthew Kerns [1:35:43]: Yeah

@Mekaiel Abdullahi [1:35:44]: Like if a new league comes in, it'll probably create like

@Trent [1:35:47]: What to do after that, once you've got the new lead, like how do you follow up with them?

@Matthew Kerns [1:35:52]: Like their name might be Billy Bob, but it's just AI transcript, so you have to confirm before it gets entered somewhere.

@Trent [1:36:02]: AI calls summaries and transcripts on the starter plan, AI call summaries and transcripts are included for calls handled by Sona. Upgrade your plan to get summermaries and transcripts for all calls. So the starter plan does not give you all calls, but we are getting all calls with the business.

@Mekaiel Abdullahi [1:36:14]: Battle.

@Trent [1:36:21]: Which is something that we're not getting with Jaber. You only get the calls that are fielded by the agent.

@Mekaiel Abdullahi [1:36:28]: One question

@Trent [1:36:30]: The receptionist

@Mekaiel Abdullahi [1:36:33]: For the free plan

@Trent [1:36:36]: No, on the paid plan, You still have to pay for the

@Mekaiel Abdullahi [1:36:41]: Oh yeah, no, I, I meant, I thought the, so I'm talking about for business. You, you should get it, right? For 23 instead of 15.

@Trent [1:36:49]: Oh no, coming back to here. The receptionist here

@Mekaiel Abdullahi [1:36:52]: Oh yeah Got you.

@Trent [1:36:54]: In robber

@Mekaiel Abdullahi [1:36:55]: Mhm.

@Trent [1:36:55]: Does not give us call recordings for actual communication between a human and a human.

@Mekaiel Abdullahi [1:36:58]: Oh yeah. Does not, yeah

@Trent [1:37:03]: Yeah, there's no transcripts for any of that. So

@Matthew Kerns [1:37:09]: Hmm

@Trent [1:37:11]: Productivity and collaboration, snippets, internal threads, shared contacts Contact notes Business hours, voicemail transcripts, call recording is automatic. Auto replies, scheduled messages, user groups, group messaging, basic call forwarding.

@Trent [1:37:32]: Call views, I don't know what that is. Call hold. Call views, automatically forward calls to another US or Canadian number, but that's

@Mekaiel Abdullahi [1:37:47]: Or

@Trent [1:37:49]: Oh, they, they don't have a comment. They don't have a Note for this Advanced call forwarding

@Mekaiel Abdullahi [1:37:58]: Automatically forwards and it's cost money.

@Trent [1:38:00]: Based on bird's powers Menus Group calling Include multiple active participants on any call. Transfers

@Trent [1:38:17]: Redirect callers to any team, member, person in your workspace externally without leaving the call? A ring order, rings one call, one phone, and if that doesn't answer, it rings the next one. So if Kelsey can't get to it, it'll pass it to Alyssa.

@Mekaiel Abdullahi [1:38:35]: Yeah

@Trent [1:38:39]: Email, slack, Zapier, SMS via API. So we can send messages, our own text messages, using an automation.

@Mekaiel Abdullahi [1:38:52]: Yeah

@Trent [1:38:52]: It links to Google Contacts, it has webhooks. Links to HubSpot, Salesforce, Jobber. Adio, and Gong. User roles in management, analytics and reporting, audit log.

@Trent [1:39:08]: And then support bubble, so. So,

@Matthew Kerns [1:39:27]: So overall, seems like quo is more Powerful Then we need to build Well, we need to see what integrations with Jouber already are built in, I guess.

@Trent [1:39:41]: Yeah, that's kind of what I was thinking was that we need to know what o does with Jaber. I think the best way to do it really is coming back to, we need to just link, just try them out. I can see if there's any information in here. No, this is API. I don't want that.

@Matthew Kerns [1:39:54]: Yeah

@Trent [1:40:00]: I wanted Resource Center Integrations, Java, here we go.

@Matthew Kerns [1:40:13]: Yeah, the

@Trent [1:40:16]: Sync call summaries and transcripts from quote to Jaber. Call clients with one click. Automattic client and request creation.

@Trent [1:40:33]: Kozek's jobber for existing clients by phone number on incoming calls. Creates placeholder client records for new callers automatically. Generates new request objects for unmatched calls. And ensures no lead or client information is lost.

@Trent [1:40:53]: So what do we think this is gonna be? I mean, It's gonna be feeding all of those calls as information into Jobber.

@Mekaiel Abdullahi [1:41:05]: Mhm

@Matthew Kerns [1:41:06]: So that's pretty similar to the receptionist.

@Trent [1:41:09]: Yeah Receptionist does that same thing AI call summary sync, automated data transfer, quote AI generates concise call summaries after each conversation, complete call transcripts sync directly to Jaber. Time stamped transcripts for easy reference, eliminates manual note taking and data entry.

@Trent [1:41:30]: And that's what it does Inside of the requests Is like an inbox of the details of the conversation.

@Matthew Kerns [1:41:41]: Mhm

@Trent [1:41:44]: It doesn't show the transcript. But it does show the summary and next steps. Click to call from Jobber.

@Matthew Kerns [1:41:55]: Interesting

@Trent [1:41:57]: Just means you can quickly get to the number and call. Per number sync settings control what syncs to Jabber. Choose what quo numbers sync to jobber. Turn sinking on and off Keep job or organized by only syncing the numbers you want.

@Trent [1:42:20]: OK, Benefits for field service teams. Streamlined workflow, create clients and requests automatically from new caller interactions. Quick context access from past conversations in Jabber.

@Trent [1:42:36]: Complete conversation history. What's that?

@Matthew Kerns [1:42:37]: OK I was saying, OK, cause the To know Past about past info in Jaber conversation, so.

@Trent [1:42:50]: Complete conversation history with detailed transcripts.

@Matthew Kerns [1:42:51]: As is

@Trent [1:42:56]: Reduced data entry with automatic synchronization. Improved service delivery, so better customer insights, full conversion context before service visits. Or conversations, sorry Historical communication patterns and preferences.

@Trent [1:43:14]: Detailed service request information from calls. Enhanced follow-up capabilities. To set it up Sign up, activate it. Install

@Trent [1:43:32]: Enable transcribe and summarize calls for phone numbers, and ensure AI summaries are activated. Verify job or account permissions, test with sample calls. Automatic synchronization is AI generated call summaries, complete conversation transcripts, call metadata.

@Trent [1:43:51]: Duration, time stamp of participants. Client identification and contact information. Data organization and jobber is structured information, new clients created automatically, Service requests are generated from the calls, call summaries attached to appropriate records.

@Trent [1:44:10]: Transcripts available for detailed review. There's a workflow integration. This is going to be interesting. Review call summaries before service visits. Use transcripts for service. Request clarification

@Trent [1:44:27]: Access complete conversation history. Plan follow-up activities based on call content. I mean it's All helps address the things he's talked about.

@Matthew Kerns [1:44:40]: Yeah, one thing I'm, I haven't seen yet is Updating the the job like it keeps talking about the requests. So there's a thing in Jaber called the job, right? And then

@Trent [1:44:51]: Yeah. There's a request and there's a job, then there's a client.

@Matthew Kerns [1:44:54]: How does it Yeah, and then there's a quote, and it's like, how do we

@Trent [1:44:58]: Yeah How do they tie together

@Matthew Kerns [1:45:03]: Yeah

@Trent [1:45:04]: I think a request is literally that. Somebody makes a phone call, they fill out your user form, they send a text. It creates a request that has to be handled. So every request has to be processed. Some way

@Matthew Kerns [1:45:20]: But they don't even use requests right now.

@Trent [1:45:21]: Right now they're not even using requests.

@Matthew Kerns [1:45:24]: Yeah

@Trent [1:45:25]: So that would be something that would be new to them.

@Matthew Kerns [1:45:30]: Yeah, but we can show them like, hey, this, these are the benefits, this is how you know workflow works, and this is how it's all more organized, maybe that'll be what they need.

@Trent [1:45:40]: Yeah, requests to me is the inbox. Of all the things that you need to handle.

@Matthew Kerns [1:45:45]: Mhm.

@Trent [1:45:48]: So, then they get turned into something, which would be potentially a quote. Quote is just where you're gonna end up You know, estimation of services or whatever and send it to them.

@Matthew Kerns [1:46:01]: Mhm

@Trent [1:46:01]: Then a job is actually doing a service call that you intend on getting paid for.

@Matthew Kerns [1:46:11]: Yup.

@Trent [1:46:11]: Then there's Notes. There was something inside Job. Visit, visit

@Matthew Kerns [1:46:18]: Yeah

@Trent [1:46:20]: So the tricky part, they were saying that they had an issue with was if you didn't have a job, But you did a visit You could link it back to the person, but it wasn't attached to the job. Like they said that you basically had to keep the job had to be in there before you do the visit.

@Matthew Kerns [1:46:43]: Yeah

@Trent [1:46:43]: So you have to be in their workflow.

@Matthew Kerns [1:46:47]: Right Cause it's like he might just get a call and just be like, OK, I'm gonna go visit the place before I even find out if we're going to give them a quote. So it's like, why do you need to to have an official paid for job before doing a a visit.

@Trent [1:47:08]: Yeah.

@Matthew Kerns [1:47:08]: I think that the way they're so in the weeds on their service fulfillment that Like If we just take the time to see what Joer offers, like we might be able to improve their workflow just by being like, here's a, here's a loom video, here's the training of how it could be done

@Matthew Kerns [1:47:29]: Like, We'll have to go in and figure out all that stuff, and then But I think we should look at what Jouber offers And then we can start adding on stuff with quo, but we need to figure out the workflow.

@Trent [1:47:44]: What is the intended? I think this is what we need to figure out. What is the intended workflow in Jobber.

@Mekaiel Abdullahi [1:47:46]: It's

@Matthew Kerns [1:47:52]: Yeah

@Trent [1:47:53]: Their bypassing, I think, one of the key components, which is requests.

@Matthew Kerns [1:47:57]: Yeah Yeah

@Trent [1:47:59]: They're just jumping straight to The other things

@Matthew Kerns [1:48:05]: Yeah, cause requests, it could be like An incoming call happens and then that, that gets logged as a request and like maybe They do a visit, like a, they go in person.

@Matthew Kerns [1:48:21]: And it's still in the request stage. But They're thinking You know, it's a visit, so it should be a job or a visit, but like If they haven't paid anything yet, then technically in the workflow. It's just at request stage. And like visit is just meant for

@Matthew Kerns [1:48:40]: Once they've paid and you're like visiting to fulfill a service or something.

@Mekaiel Abdullahi [1:48:48]: I agree

@Trent [1:48:49]: So here's some limit.

@Mekaiel Abdullahi [1:48:50]: It's the way that you're using Jaber, I feel like. Because, yeah, like the way it's intended to and the way they're using it, I don't think is lining up.

@Trent [1:48:59]: No, I don't think so either. I think that we could probably improve their workflow just by understanding how the the tool is intended to be used, and just put some

@Mekaiel Abdullahi [1:49:08]: Structure

@Trent [1:49:09]: Some structure around it, yeah So Here's some limitations of the synchronization. I don't know if you saw this or not, but Client information updated in jober doesn't sink back to quo. This is a one-way street So quote, things come in the quo

@Trent [1:49:26]: And then they disappear or no they don't disappear. They go

@Matthew Kerns [1:49:33]: Yeah, they get updated and

@Trent [1:49:33]: So they They get, they go, yeah, they go from quote to jobber, but it doesn't go from jobber to quote.

@Matthew Kerns [1:49:35]: But when

@Trent [1:49:39]: Which we could, we could patch some of that, we prefer not to. But we could probably patch some of it if we needed to.

@Mekaiel Abdullahi [1:49:47]: Mhm

@Trent [1:49:49]: The APIs

@Matthew Kerns [1:49:49]: I mean like You mean like detect when something gets updated in Jobber and then update quo. Yeah, definitely

@Trent [1:49:56]: Depending on what it is. If, if we discover a hole or a gap that's causing problems. One of the problems I think might happen is they treat the jobber as the central like source of truth, right? So if anything in quo is relative to something that happened in Jouber

@Matthew Kerns [1:50:08]: Yeah

@Trent [1:50:15]: It won't know it

@Matthew Kerns [1:50:19]: Right

@Trent [1:50:20]: I'm not, I'm not sure what those are though. Is it the contacts, maybe, like cause it does say client information doesn't sink backwards. They're promising in the future that they may include bidirectional sync.

@Trent [1:50:39]: All right, so here's best practices. This is useful for us as well, right? Effective configuration, enable call summaries for client facing phone numbers. Test configuration or test integration with sample calls, train the team on accessing synced data in Jabber.

@Trent [1:50:56]: Regular review of client creation and reg request generation. So it looks like to me, that's all it does. It only creates clients and requests.

@Matthew Kerns [1:51:10]: Yeah.

@Trent [1:51:11]: At that point, it's been handed off to the jobber process.

@Matthew Kerns [1:51:16]: Yeah, and that's probably because of the lack of bidirectional sync. Like it's It's one way So you just

@Trent [1:51:27]: With the purpose of the other stuff and Jabber being in quote.

@Matthew Kerns [1:51:38]: So like, well, if we want Say there's a phone call that's about an existing client If Quo doesn't know the latest updates from Jouber, then they can't Look at the existing notes and say like, OK, we already know this stuff, that's just add this one sentence that's new information.

@Matthew Kerns [1:51:58]: Right? To the notes

@Trent [1:52:01]: Yeah, but I don't think that even, even the receptionist doesn't really do that, right? So like if we look at the two tools that we're looking at, neither one of them do that.

@Matthew Kerns [1:52:07]: Yeah, no Yeah Yeah, I think receptionist is also like, cause they're they're just building, they're just building the first thing, right? Like they've just built the first thing, which is integration with the client because

@Trent [1:52:27]: Instant calls automatically.

@Matthew Kerns [1:52:28]: That's Yeah, because that's like the highest. Value to the business. Like fielding calls, cause it's, it's like Like what Kelsey is saying right now, like wasted time from With zero filtering on his phone number, he just gets calls from everybody.

@Trent [1:52:48]: Yep So it says something down here To maximize value, one of the mentions is coordinate with job or scheduling and quoting features. Does that mean that you manually coordinate it? It kind of sounds like it.

@Trent [1:53:05]: Like It creates a client, it creates a request, and then you have to follow up with scheduling and quoting.

@Matthew Kerns [1:53:14]: Yeah.

@Trent [1:53:17]: Data management, maintaining quality monitor automatic client creation for accuracy. Regular cleanup of placeholder client records. So There may be an automation that we may have to do. Or at least put an SOP in place as part of the workflow or something, that they have to go in and review

@Trent [1:53:38]: Placeholder client records, because what can happen from quo is you get a phone call from some random number It'll automatically take that and put it into jobber.

@Matthew Kerns [1:53:49]: Mhm

@Trent [1:53:50]: But it it may never get, nothing else happens to it. It's possible, right?

@Matthew Kerns [1:53:56]: Yeah, and it's possible they don't even say their name, so it's just an empty

@Trent [1:54:01]: We

@Matthew Kerns [1:54:02]: Phone number, yeah

@Trent [1:54:04]: Yeah, it may have a transcript, it may have a, a phone number, but it doesn't have contact details or any request that's attached to it. It literally is just Like no actual request, it literally is just An empty client

@Matthew Kerns [1:54:21]: Mhm

@Trent [1:54:22]: An empty contact in the records. And ensure call summary quality through proper conversations. Review transcript accuracy and completeness. So, I mean That's kind of where we're at with that

@Trent [1:54:38]: You know something that I didn't see Which we could probably figure out. Is it doesn't do scheduling automatically.

@Matthew Kerns [1:54:49]: So o doesn't do scheduling of, yeah. Where the job or receptionist did have the integration.

@Trent [1:54:58]: Correct. Correct. We would have to build something on top of quo and Joer to To do that

@Matthew Kerns [1:55:10]: Or does the Jaber receptionist do that? If so you're saying if we don't use Java receptionists, then we build it.

@Trent [1:55:16]: Yeah, yeah, if we don't use the Java receptionist.

@Matthew Kerns [1:55:20]: OK Yeah.

@Trent [1:55:44]: You can connect your own cloud or cloud or chat GBT Integrated to it, so you can have more thorough conversation with it. Bringso directly into your AI assistant. You can send texts

@Matthew Kerns [1:55:56]: Mhm

@Trent [1:56:00]: Check messages Pull call transcripts using natural conversation, no clicking around or switching apps. Think of it as a quo remote inside your AI chat, so you could take Chat GBT. He's been playing with a, and he could link it to Quo, and he could actually have a conversation with Chad GBT to do something useful.

@Matthew Kerns [1:56:17]: Yeah

@Trent [1:56:24]: In quo, cause he talked about it can't do shit, right? But

@Matthew Kerns [1:56:29]: Yeah, but it might be like, it still can't do shit, like it can read stuff.

@Trent [1:56:35]: Yeah, you're right. You're right. I've experienced that too.

@Matthew Kerns [1:56:40]: Yeah

@Trent [1:56:45]: What it can do, here you go Pull my last 100 calls from a number and summarize them. Send a text OK?

@Matthew Kerns [1:56:56]: Hmm

@Trent [1:56:58]: I wasn't expecting to send a text, check recent messages

@Matthew Kerns [1:57:01]: Yeah

@Trent [1:57:03]: Get voicemail transcripts. Send bulk messages To the entire crew

@Matthew Kerns [1:57:12]: Well.

@Trent [1:57:13]: Create a contact That's nice, create a contact.

@Matthew Kerns [1:57:19]: Yeah

@Trent [1:57:20]: Review message history, get all messages from this morning on our support line. Hm. Hm Hm I mean, those are all maybe

@Matthew Kerns [1:57:35]: It's also

@Trent [1:57:36]: Bonus functionalities that we may have Wanted to implement in the future, maybe. But

@Matthew Kerns [1:57:43]: Mhm

@Trent [1:57:44]: They're kind of here now

@Matthew Kerns [1:57:45]: It's also It's also in beta though, so it's promising these, but we don't know how functional it is. It's sort of like, yeah, we're gonna have to try out

@Trent [1:57:53]: True.

@Matthew Kerns [1:57:57]: Maybe one of the best things after we get done looking through the docks is

@Trent [1:57:57]: I think

@Matthew Kerns [1:58:02]: To try them out and then keep probably looking back through the docs, but

@Trent [1:58:08]: Keep in mind that this is, keep in mind that this is an MCP server that we could tap into. They have an API, but they have an MCP server. Sometimes I found the MCP server is more limited than the API.

@Matthew Kerns [1:58:09]: Yeah. Yeah, cause now

@Trent [1:58:22]: So Yeah, but at the same time, it enables the ability to connect to your mobile app. So for example, your phone, And talk to your talk to your phone to get the information.

@Matthew Kerns [1:58:32]: Real

@Trent [1:58:36]: And it looks like what you can do is you can send a text message, send bulk messages, check recent messages, get call transcripts, and you can create contacts. So it doesn't say you can get contacts. So I don't know where that comes into play.

@Trent [1:58:55]: Seems like if you can create them, you should be able to read them too, but

@Matthew Kerns [1:58:56]: Yeah Yeah

@Trent [1:59:00]: There's no reason that we couldn't give these tools. Our own tools in like N8N. We could create these tools In NAN and do the same thing if we wanted to. And we could actually do that for Jouber.

@Trent [1:59:17]: If we want to I guess what I'm saying is that we're not, this is an example of things that we can add on that are AI features that are potentially useful for Kelsey.

@Matthew Kerns [1:59:20]: So Yeah If there's something in official documentation and like Jabber and quo.

@Matthew Kerns [1:59:42]: That's like already been like tested thoroughly, like they've launched it, they've they've tested it with test users and like test. People, so if we choose to build it ourselves, we're signing up for

@Trent [1:59:57]: Support me

@Matthew Kerns [1:59:57]: A bunch of testing and yeah, and we have to test all the edge cases. And I think there's gonna be plenty of work to do I mean, there's plenty of work already just figuring out what the heck we should have them use,

@Trent [2:00:14]: Yeah.

@Matthew Kerns [2:00:16]: Imagine if There's already things built that we just show them how to use and then send them on their way and they have an improved workflow like that's also a possibility where we don't even build anything.

@Trent [2:00:29]: I mean, you mean you mean like just let them use Jobber and don't implement anything else, just literally just Jobber. And just teach them how to use it properly.

@Matthew Kerns [2:00:37]: Yeah Yeah

@Trent [2:00:41]: Is also an option. I mean, we didn't tell them that's what we're going to give them, but at the same time, it's an option.

@Matthew Kerns [2:00:48]: Yeah, and then we also did say like we don't want to build something if it's not going to be the most, it's not going to be useful and cost effective. So, like showing them An impro, all, all they want at the end of the day, all Kelsey wants is an improved life experience. So,

@Trent [2:01:05]: Yeah

@Matthew Kerns [2:01:06]: If we just show him the jobber features, there's probably going to be some stuff in there within Jora that we need to build that like Alyssa doesn't have time to build, like, like setting up the escalation policy for the job or receptionist, for example, or like setting up routing within Jobber.

@Matthew Kerns [2:01:24]: There's probably limitations, so we're gonna have to sort out like, you know, what we onboard them with, of course, but

@Trent [2:01:31]: Yeah.

@Matthew Kerns [2:01:31]: I'm just saying like we shouldn't be just looking for What should we build, we should look for

@Mekaiel Abdullahi [2:01:37]: How to improve what you're using.

@Trent [2:01:37]: Good Yeah

@Matthew Kerns [2:01:40]: Yeah. Get to the outcome. Use stuff that's already built, ideally, and then

@Mekaiel Abdullahi [2:01:46]: Yeah

@Matthew Kerns [2:01:47]: If we absolutely need to, then we start, then we build something.

@Trent [2:01:52]: So here's, here's my, the, so where I'm really,

@Matthew Kerns [2:01:52]: I think

@Trent [2:01:59]: Pro quo, pro quo, OK.

@Mekaiel Abdullahi [2:02:03]: I see what she did

@Trent [2:02:05]: Yeah, I'm really, I'm really pro quo because of the transcripts for all the calls.

@Mekaiel Abdullahi [2:02:12]: That's ideal

@Matthew Kerns [2:02:14]: Mhm

@Mekaiel Abdullahi [2:02:17]: That's kind of like our main reason, right

@Trent [2:02:19]: Yeah That, that like we understand that that is like Where we can really add value into the future. And I think it will add value now just with the core functionality, with without

@Matthew Kerns [2:02:28]: Yep.

@Trent [2:02:32]: Us building an automation.

@Matthew Kerns [2:02:36]: Mhm

@Trent [2:02:37]: I, I'm actually starting to think that if we do quo Get him his chat GPT hooked up to Quo. Get quo functioning well with Jaber. Refine their process in Jaber.

@Matthew Kerns [2:02:54]: Mhm

@Trent [2:02:55]: I mean, he's they're gonna see a wildly different Communication

@Mekaiel Abdullahi [2:02:59]: OK.

@Trent [2:03:00]: Capability, just by doing those things.

@Mekaiel Abdullahi [2:03:02]: And that's exactly what we promised too, right? Like, we only promised to introduce Quo. That was kind of like the only new tool we were gonna introduce, right? But I think a lot of these, I think a lot of these cases we're gonna see is we're gonna walk into small businesses and they're already going to have a tool set, but probably only gonna be utilizing like 50%, 60% of those tools. So I think a lot of our job is gonna be how, how do we unlock their understanding of the tools and how to use the tools to their full capacity, you know. And our jobs is engineers develop like we don't always have to build new solutions, like we just got to get them to understand what

@Trent [2:03:11]: So

@Mekaiel Abdullahi [2:03:37]: Tools they have and how to use them properly.

@Trent [2:03:39]: Yeah I, I think that we only build a tool where the gap exists. Right, right now, like, we may be building something for him in the future, but remember we're just trying to do a quick win to set us up for a few.

@Mekaiel Abdullahi [2:03:45]: I agree. Yeah Yeah Yep

@Trent [2:03:54]: So I'm thinking that right now, let's try to see if we can maximize just

@Mekaiel Abdullahi [2:04:00]: What he has

@Trent [2:04:02]: And that that really I think was the intention anyway, right? So, I don't know how much do we need to do with Implementing N8N workflows. For their operations in phase one.

@Trent [2:04:19]: Right? I don't know if we need to do a lot with that. I think that we can get really, really far.

@Matthew Kerns [2:04:21]: Yeah

@Trent [2:04:27]: By just using quo and Jaber, and I think that we should just Point chat GPT if he's paying for it anyway. We should just point it to Quo to give him the power of being able to communicate the quo.

@Matthew Kerns [2:04:42]: Mhm

@Mekaiel Abdullahi [2:04:42]: I agree. We, that's a start, right? And then if that gets him to the result where you said, like, cool, we could do whatever else, you know.

@Matthew Kerns [2:04:53]: Yeah Does Jobber have a Chat GBT Integration

@Trent [2:05:01]: We'll see Let's see. Let's see

@Mekaiel Abdullahi [2:05:06]: I have What do you mean by pointing it to Chachibichi, like pointing quote ChaiBT.

@Trent [2:05:12]: Well, the other way around. So he can use his phone with the chat GPT app.

@Mekaiel Abdullahi [2:05:17]: Mhm

@Trent [2:05:17]: To talk to Quo.

@Mekaiel Abdullahi [2:05:19]: Nice. OK

@Trent [2:05:19]: So then what he can do You, you missed out on this one while we were having the conversation. Where did it go? Oh it's in here, right here. So what he can do, for example, He can analyze call patterns. So for example, he asks chat GBT or Claude.

@Trent [2:05:38]: Pull my last 100 calls from this phone number and summarize what questions do prospects ask most. Send a text message to this phone number from my number, running 10 minutes late. Check recent messages, show the last 10 messages from this number.

@Trent [2:05:57]: Get voicemail transcripts, pull today's voicemails for our main number.

@Mekaiel Abdullahi [2:06:02]: I might need, quote, forget all that, bro bro.

@Trent [2:06:06]: Send bulk messages

@Mekaiel Abdullahi [2:06:07]: Yeah.

@Trent [2:06:08]: Send this update to the entire crew. Job site moved to Oak Street. Create a contact, add Mary Lopez from Acme, HVAC with this phone number, Roll dispatcher. Review message history, get all messages from this morning on our support line.

@Mekaiel Abdullahi [2:06:28]: Quo and Jack CBT is like what Siri was supposed to be. Like

@Trent [2:06:34]: In some ways. So you can send a message, you can send bulk messages, you can check recent messages. You can get call transcripts and you can create contacts. Those are the things you can do.

@Matthew Kerns [2:06:46]: What if you click create contexts right there.

@Trent [2:06:49]: Add new context to o workspace with name, company, phone, and email.

@Matthew Kerns [2:06:54]: OK

@Mekaiel Abdullahi [2:06:54]: And you can just use the voice thing on ChatGVT to do that, like that's so far, like.

@Trent [2:06:58]: Yeah. Yep. We're not building any any new user interfaces or automations that we have to support. All we're doing is connecting an existing app to a tool that we're putting in place. That collects the data That he needs

@Mekaiel Abdullahi [2:07:13]: He's gonna freak out when you can talk to Chad GBT and like control his business. He's gonna, he's absolutely gonna lose the shit.

@Trent [2:07:21]: I mean, I think that's a wow factor that is truly useful though. I think it's useful for what he does.

@Mekaiel Abdullahi [2:07:23]: Yeah Mhm

@Trent [2:07:29]: So, anyway, I

@Mekaiel Abdullahi [2:07:29]: I agree

@Trent [2:07:31]: I think that we've come up with a lot of Good ideas in this call, plus the plotter mechanic's call Do you think that there's value right now in just stopping our huddle. Take a break Maybe take the transcripts and do something with them.

@Mekaiel Abdullahi [2:07:51]: Yeah, I got a hop for 3:30, but yeah, I can, I can, whatever you guys need me to.

@Trent [2:07:56]: At 5 o'clock Eastern, We've got the call with SS Wolf sheds. I would like to have the next hour. To do other things.

@Matthew Kerns [2:08:12]: Yeah

@Trent [2:08:15]: Which is roughly how much we have

@Matthew Kerns [2:08:16]: We need to We need to figure out, I guess we've done a lot of work on plotter. We need to, we need to process the transcripts. And put together a plan I can, I can do that.

@Matthew Kerns [2:08:34]: I'm just thinking what time cause I also wanna have a little break before the SNS call, so I can be fully present there.

@Trent [2:08:41]: Well, if you want to do stuff after SS Wolfsh sheds. We can do that too

@Mekaiel Abdullahi [2:08:46]: Yeah, I feel you we stop on potter for a bit at least, you know, that way you guys can do other things as well. I think we got far enough on plotter.

@Matthew Kerns [2:08:46]: Yeah

@Mekaiel Abdullahi [2:08:55]: For now, at least. We can always revisit later today, and then that way, We have an hour and a half till SNS. And then we can just

@Trent [2:09:03]: Matthew also, yeah, sorry, I didn't mean to talk over it.

@Mekaiel Abdullahi [2:09:07]: No, no worries

@Trent [2:09:07]: The delay.

@Mekaiel Abdullahi [2:09:09]: Yeah.

@Trent [2:09:11]: Matthew also Don't forget that even though we just talked about maybe we don't even use NAN and we can get a huge amount of value just by refining their process and adding that tool only.

@Matthew Kerns [2:09:23]: Mhm

@Trent [2:09:25]: We talked about how do we evaluate their existing situation. We talked about maybe using NAN in the API to go out and get the data and put it into a database or something.

@Matthew Kerns [2:09:38]: Right

@Trent [2:09:39]: I don't know

@Matthew Kerns [2:09:39]: So we can analyze

@Trent [2:09:41]: Yet

@Matthew Kerns [2:09:42]: Yeah

@Trent [2:09:44]: For analysis. We can ask Chat GBT or not chatGBT Claude, to go out to the database and try to work through some of this.

@Matthew Kerns [2:09:55]: Yeah, and there's no Jaber doesn't, I don't think has an MCP server so we can't. Connect to Jabber,

@Trent [2:10:02]: Is that what you just found? Well, we, we can. We can. Using the agentic stuff that I created. Would just add a job or module.

@Matthew Kerns [2:10:09]: Yeah. Yeah So like

@Trent [2:10:15]: You want

@Matthew Kerns [2:10:17]: There's like, and, and all we have to do is set up NAN like I basically have already set up in any then node for Dauber. So we can connect to their APIs through NAN

@Trent [2:10:34]: But my here's another question though is that do we need, would it, would it make sense if we, if we're literally only trying to do analysis.

@Matthew Kerns [2:10:35]: Yeah, we can Yeah Mhm

@Trent [2:10:47]: Would we Be better to just go, if we're not going to do an automation For them. Would it make more sense to just go straight to having Claude build something. To interact with the API. And then

@Matthew Kerns [2:11:01]: But I think one thing that you pointed out before was, we're gonna run into limits, like I already ran into a throttling limit, so we're just gonna need to pull it all and store it somewhere so we don't have to get the data through the API.

@Trent [2:11:16]: Yeah, I think that's actually best anyway. I don't think it's a good idea to have Claude.

@Matthew Kerns [2:11:16]: Or if it's then

@Trent [2:11:21]: Access their API because I don't know what it'll do.

@Matthew Kerns [2:11:26]: Yeah Yeah, like I'm, I'm trying to limit the permissions of the developer app to just be read only so that it can't, even if it tried to.

@Trent [2:11:38]: Yeah, OK, that's good. Well, so, yeah, I think that if we're going to do that, what we need to do is just set up, use your N8N Node And then if we hit rate limits, then we'll have to back it off.

@Matthew Kerns [2:11:54]: Mhm.

@Trent [2:11:54]: Right? Wait for some period of time, and then only query every so often. And then store it into a database and then we can use the database to to query.

@Matthew Kerns [2:12:01]: Yeah

@Trent [2:12:05]: With Claude

@Matthew Kerns [2:12:08]: Yeah, we can even set it up to run in the background until it gets all the clients into the the database.

@Trent [2:12:15]: Yeah So, Just think on that. We don't have to work on it right now, but have that as a thing.

@Matthew Kerns [2:12:26]: Yeah, yeah

@Mekaiel Abdullahi [2:12:26]: I gotta drop both on Tokyo.

@Trent [2:12:28]: OK, yep, see you come.

@Matthew Kerns [2:12:30]: McGill

@Trent [2:12:32]: Yeah, so anyway, we got in the transcript now, so it'll come up.

@Matthew Kerns [2:12:36]: Yeah, we do got to make sure that we There's so much data in these transcripts that I feel like even though we think it's all captured, but if nobody processes the transcript, then it's it's still kind of gets lost, you know.

@Trent [2:12:50]: Uh-huh, well, that's what I feel too, is like we have a lot of stuff that's valuable stuff that we're putting in transcripts and right now they're just

@Matthew Kerns [2:12:59]: Yeah, somewhere

@Trent [2:13:00]: They're just floating out there right now. So.

@Matthew Kerns [2:13:02]: Yeah

@Trent [2:13:04]: But anyway

@Matthew Kerns [2:13:05]: Yeah

@Trent [2:13:06]: Think on that, mostly focused on plotter for that purpose, but I can help with trying to set up databases and Give us a way to store it so that we can process it later.

@Matthew Kerns [2:13:19]: Yeah, let's, let's think about it, Yeah, we just have to figure out Our objectives and stuff. Probably just taking a break will help get some of the stuff more clear too.

@Trent [2:13:31]: Yeah, I need a break, so I know you do too. So let's, let's just go ahead and just shut her down, go take a break, and then we'll come back for as this wolf she, OK?

@Matthew Kerns [2:13:40]: OK, sounds good. All right.

@Trent [2:13:41]: Thanks, appreciate you See ya.

@Matthew Kerns [2:13:44]: Yeah, I appreciate you too. See ya.