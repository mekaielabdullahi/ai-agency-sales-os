# Transcript: Plotter Mechanix Phase 1 Quo to Jobber Integration Handoff Call

**Meeting Date:** 2026-01-23
**Duration:** ~2h

---

[00:00:01] **Trent Christopher**: And talk a little bit about how I went about testing it and just kind of see what feedback you have, what thoughts you have, and just try to get an idea of anything that we should prepare for before I just flip it on.

[00:00:14] **Trent Christopher**: Now, one thing I'll say before we even worry too much about, I think the blast radius is pretty small.

[00:00:25] **Trent Christopher**: Like the risk is relatively small.

[00:00:28] **Trent Christopher**: My biggest concern is going to be making sure contacts don't get jacked up.

[00:00:34] **Trent Christopher**: So we can get into that in just a second.

[00:00:36] **Trent Christopher**: So I want to show you first the outcome and then we'll get into the details.

[00:00:43] **Trent Christopher**: Okay.

[00:00:44] **Trent Christopher**: So here, I don't want to do that one yet.

[00:00:47] **Trent Christopher**: Let's do, this is all in mine, my jobber instance.

[00:00:52] **Trent Christopher**: Um, and this is all real calls, but some of them have come in from.

[00:00:59] **Trent Christopher**: Quo, I think, while I was testing, because I have Quo connected, like as they make phone calls or whatever, it still comes in here.

[00:01:08] **Trent Christopher**: So it's not completely just testing.

[00:01:11] **Trent Christopher**: So we'll just check it out.

[00:01:14] **Trent Christopher**: So all of these are requests that came in.

[00:01:20] **Trent Christopher**: Can you show?

[00:01:21] **Matthew Kerns**: I think you're not sharing the screen.

[00:01:23] **Matthew Kerns**: Oh, yeah.

[00:01:24] **Trent Christopher**: Let's try doing that.

[00:01:25] **Trent Christopher**: That really helps.

[00:01:26] **Trent Christopher**: Makes it a lot easier.

[00:01:29] **Trent Christopher**: All right.

[00:01:29] **Trent Christopher**: So can you see it now?

[00:01:35] **Trent Christopher**: Yep.

[00:01:36] **Matthew Kerns**: Okay.

[00:01:37] **Matthew Kerns**: All right.

[00:01:38] **Trent Christopher**: So these are all requests that have come in from the jobber from N8N.

[00:01:46] **Trent Christopher**: So none of this is built in Quo integration at all.

[00:01:52] **Trent Christopher**: This is all.

[00:01:54] **Trent Christopher**: All that.

[00:01:55] **Trent Christopher**: So this one here is Lalo.

[00:01:59] **Trent Christopher**: So.

[00:02:00] **Trent Christopher**: This one here in particular, what's notable about this one is I don't think there was a contact existing, and it picked up Lalo in the conversation.

[00:02:11] **Trent Christopher**: Okay.

[00:02:12] **Trent Christopher**: Has the number, talks about Roland printers, two different Roland printers, and the summary is in the middle.

[00:02:25] **Trent Christopher**: The notes are on the right.

[00:02:26] **Trent Christopher**: Now, if any additional notes come in, they get added to this.

[00:02:31] **Trent Christopher**: The newest goes to the top.

[00:02:33] **Trent Christopher**: The older ones, it's in, we want to say, descending order.

[00:02:41] **Trent Christopher**: So the newest is at the top.

[00:02:45] **Matthew Kerns**: I'm currently not refreshing the details in the middle.

[00:02:49] **Trent Christopher**: I'm only taking the first event, the first note, in the middle.

[00:02:56] **Matthew Kerns**: Okay.

[00:02:58] **Matthew Kerns**: I didn't know

[00:03:00] **Trent Christopher**: I if I wanted to get into the complexity of trying to refresh and update that.

[00:03:04] **Matthew Kerns**: So, sorry, so you said with, there's a, so the notes, the new notes are on the right at the top.

[00:03:10] **Matthew Kerns**: The newest ones come in at the top.

[00:03:13] **Matthew Kerns**: And with the overview, it's not refreshing with the latest, right?

[00:03:17] **Matthew Kerns**: No, it's only taking the first note that comes in.

[00:03:20] **Trent Christopher**: Most of the time, it's only going to be one, but there will be an occasional multiple note situation that will come in.

[00:03:29] **Trent Christopher**: And if, if it is in a new or converted status, not archived, then it will continue to add notes to this.

[00:03:44] **Trent Christopher**: Okay.

[00:03:45] **Matthew Kerns**: Okay.

[00:03:46] **Trent Christopher**: So that's what it's looking for.

[00:03:47] **Trent Christopher**: It's looking for the status to, to be something other than new.

[00:03:53] **Trent Christopher**: Yeah.

[00:03:54] **Trent Christopher**: Basically like in progress.

[00:03:55] **Trent Christopher**: If it's in progress, it just leaves, it continues to add notes to it.

[00:03:59] **Trent Christopher**: And you're Bye.

[00:03:59] **Trent Christopher**: Bye.

[00:03:59] **Trent Christopher**: Bye.

[00:03:59] **Trent Christopher**: Bye.

[00:03:59] **Trent Christopher**: Bye.

[00:03:59] **Trent Christopher**: you.

[00:04:00] **Matthew Kerns**: I guess the only thing in the overview, the main thing that goes out of date is just those next steps.

[00:04:10] **Matthew Kerns**: Do the notes, when there's notes generated on the right, is that just transcript?

[00:04:18] **Trent Christopher**: No, I've removed the transcript because what happens is that when you go, for example, let's just turn one of these into, let's turn Lalo into a job.

[00:04:29] **Trent Christopher**: So I'm going to convert it to a job.

[00:04:31] **Trent Christopher**: So when I convert it to a job, the notes carry over.

[00:04:37] **Trent Christopher**: You can see the request on the right, but if you scroll down the notes, length notes.

[00:04:45] **Trent Christopher**: So if you do length notes, you'll see the length notes.

[00:04:48] **Trent Christopher**: Now, here's the thing.

[00:04:52] **Trent Christopher**: The links notes will continue to build.

[00:04:56] **Trent Christopher**: Like if you add more, this list will.

[00:04:59] **Trent Christopher**: next next time.

[00:04:59] **Trent Christopher**: there.

[00:04:59] **Trent Christopher**: you.

[00:05:00] **Trent Christopher**: Get longer.

[00:05:01] **Trent Christopher**: If you were to have a transcript every single time that you had a call with them, even just the very first one, it can be really long.

[00:05:11] **Trent Christopher**: So the decision that I made, and it was kind of confirmed by Kelsey, was to just have the link in the, in here.

[00:05:21] **Trent Christopher**: Now, in this instance, it didn't grab the app link because of, I actually don't know why it didn't grab the app link, but it's got the web link so you can click on it to go to the web.

[00:05:33] **Trent Christopher**: But there's also in a real world scenario, this might just be because of testing.

[00:05:37] **Trent Christopher**: didn't have the right data or something that came in.

[00:05:41] **Trent Christopher**: So let me see if I go to requests and I go to like one of these here.

[00:05:47] **Trent Christopher**: Yeah.

[00:05:47] **Trent Christopher**: So this app link, it's a deep link that when you, if you open up the app on your phone, you can touch that link and it'll take you to the conversation for your app on your phone.

[00:05:59] **Trent Christopher**: Cool.

[00:05:59] **Trent Christopher**: So

[00:06:00] **Matthew Kerns**: So does the web link not redirect you to the app?

[00:06:04] **Matthew Kerns**: Nope.

[00:06:05] **Trent Christopher**: I don't know why.

[00:06:07] **Trent Christopher**: It only goes to the web.

[00:06:09] **Trent Christopher**: So it'll take you to Quo on the web browser on your phone.

[00:06:13] **Trent Christopher**: Then you have to log in and then you're still inside the web interface in Quo on the phone.

[00:06:22] **Trent Christopher**: So I was like, okay, this is stupid.

[00:06:25] **Matthew Kerns**: They need to update that at some point and maybe they will.

[00:06:29] **Matthew Kerns**: Yeah, that's stupid.

[00:06:31] **Trent Christopher**: So we should be able to redirect it.

[00:06:32] **Trent Christopher**: I couldn't figure out how to do it.

[00:06:34] **Trent Christopher**: I was like, is there something wrong with my phone?

[00:06:37] **Trent Christopher**: But I gave the link to Claude and just talked to it saying, hey, what's going on here?

[00:06:42] **Trent Christopher**: And I said, well, it probably doesn't redirect because there's a hook or something in the app on the phone.

[00:06:49] **Trent Christopher**: It listens for that redirect or something.

[00:06:52] **Matthew Kerns**: Yeah, we work on that at Alexa for apps.

[00:06:58] **Matthew Kerns**: We're trying to get the deep link.

[00:07:13] **Trent Christopher**: I tested this Quo link on the app on my phone, and it works.

[00:07:19] **Trent Christopher**: I tested the two.

[00:07:21] **Trent Christopher**: You touch the web, it goes to your web browser.

[00:07:24] **Trent Christopher**: You touch the Quo, and it goes to the web app.

[00:07:28] **Trent Christopher**: And do you have Android or iPhone?

[00:07:31] **Matthew Kerns**: I have iPhone.

[00:07:32] **Trent Christopher**: Okay.

[00:07:33] **Matthew Kerns**: So yeah, I'm not sure, but I think the deep link for Android versus iPhone is different for the app.

[00:07:42] **Matthew Kerns**: Okay.

[00:07:43] **Trent Christopher**: Well, regardless, they have iPhones for now, but it's functional.

[00:07:50] **Trent Christopher**: So that gives you the ability to go and listen to the call and read the transcript, and you can read the summary that's inside of.

[00:07:59] **Trent Christopher**: specific Okay.

[00:07:59] **Trent Christopher**: All

[00:08:00] **Trent Christopher**: Whoa, as well.

[00:08:01] **Trent Christopher**: So you can get more detail by clicking on the link.

[00:08:04] **Trent Christopher**: So to prevent cluttering of the system, give them the link to go into more detail, but try to bring and surface as much content as possible.

[00:08:16] **Trent Christopher**: That's relevant.

[00:08:17] **Trent Christopher**: Yep.

[00:08:19] **Trent Christopher**: Um, they will have to understand that this is not going to be perfect.

[00:08:23] **Trent Christopher**: The goal is to get an 80% or better.

[00:08:26] **Trent Christopher**: Yeah.

[00:08:27] **Matthew Kerns**: Right.

[00:08:28] **Trent Christopher**: So it, the better, the they get at asking questions and being, um, like dictating it well, so that the transcription can be good, the better we can, you know, the better results are going get.

[00:08:43] **Matthew Kerns**: Yeah.

[00:08:44] **Matthew Kerns**: And like, since we're a transformation partner, like we're not just going away after we deliver it, like we'll be there.

[00:08:50] **Trent Christopher**: We can, we can work on this by capturing all of these and then trying to work on making it better.

[00:08:59] **Trent Christopher**: .

[00:09:00] **Matthew Kerns**: Yeah, I want to, I kind of want it to be like directed by them.

[00:09:05] **Matthew Kerns**: So like things that they're annoyed with, it can report to us like once a week or something, like they record it somewhere and then they tell us every so often, because that way we know what's actually annoying because we're going to just want to, we're just going to want to fix everything, but it might not even matter to them.

[00:09:21] **Matthew Kerns**: So, yeah, exactly.

[00:09:23] **Trent Christopher**: We're going to be very detailed in what we're trying to focus on.

[00:09:26] **Trent Christopher**: It may not be a big deal to them at all.

[00:09:27] **Trent Christopher**: Right.

[00:09:28] **Matthew Kerns**: Be wasting our time.

[00:09:29] **Trent Christopher**: So, um, but yeah, so generally speaking, um, so coming back to the transcript problem, okay, is that, yeah, it clutters up the web interface, but it's even worse on the phone.

[00:09:45] **Trent Christopher**: And Kelsey's the one that uses the, he only uses his phone.

[00:09:49] **Trent Christopher**: Yeah, doesn't get onto the web app.

[00:09:52] **Trent Christopher**: So when you open it up and you have a big long transcript, like scroll forever to get to the notes.

[00:09:59] **Trent Christopher**: So like.

[00:09:59] **Trent Christopher**: Okay.

[00:10:00] **Trent Christopher**: To get to the bottom of it.

[00:10:01] **Trent Christopher**: So I was like, you know what, we're just gonna get rid of the transcript and give them a link.

[00:10:04] **Trent Christopher**: So yeah, so that's, that was the best way I could think to solve that problem.

[00:10:11] **Trent Christopher**: So going back to requests, looking at some of these, this here is Logan Street.

[00:10:18] **Trent Christopher**: The information did not all, you can actually see some of it came from the conversation, it looks like.

[00:10:27] **Trent Christopher**: Um, so it extracted a bunch of different things, but I ran into issues with like this TX 3000 and TM 305.

[00:10:34] **Trent Christopher**: It was like spelling out the numbers.

[00:10:37] **Trent Christopher**: Um, so I had to get that to be correct.

[00:10:41] **Trent Christopher**: Um, okay.

[00:10:43] **Trent Christopher**: How did you get that to be fixed?

[00:10:46] **Trent Christopher**: Claude, to be honest, I just, I just had Opus 4.5.

[00:10:52] **Trent Christopher**: I said, Hey, look, I gave it a screenshot and said, this is not supposed to be right.

[00:10:56] **Trent Christopher**: Or this, this is supposed to be, if it's a spelled out number.

[00:11:00] **Trent Christopher**: So to a model number of a printer, it needs to be numbers.

[00:11:05] **Trent Christopher**: Okay.

[00:11:06] **Matthew Kerns**: So that's part of the instruction in the NNN workflow?

[00:11:11] **Matthew Kerns**: Yeah, it's part of the prompt.

[00:11:13] **Matthew Kerns**: Okay.

[00:11:14] **Matthew Kerns**: Got it.

[00:11:15] **Matthew Kerns**: Yeah, to AI.

[00:11:17] **Trent Christopher**: So there's that.

[00:11:20] **Trent Christopher**: We're pulling out all these different things.

[00:11:22] **Trent Christopher**: We're tagging calls.

[00:11:23] **Trent Christopher**: So like this says service and we'll have to maybe ask them for feedback on some of that.

[00:11:28] **Trent Christopher**: But some of them will say accounting.

[00:11:32] **Trent Christopher**: Some of them will say service.

[00:11:33] **Trent Christopher**: Some of them say supplies, but some of them are indeterminate.

[00:11:40] **Trent Christopher**: So it doesn't have a tag.

[00:11:45] **Trent Christopher**: It doesn't know based on the conversation.

[00:11:48] **Trent Christopher**: Right.

[00:11:50] **Trent Christopher**: So they have to go through them to understand them in some way, shape or form.

[00:11:55] **Trent Christopher**: But if we look at these, let's see here.

[00:11:58] **Trent Christopher**: So if we look at this.

[00:12:00] **Trent Christopher**: This one right here, this is an interesting one that is has to do with the messiness of Kelsey's contacts.

[00:12:08] **Trent Christopher**: So this contact where what happens is that we receive a webhook about the transcript from Quo and that transcript has the contact ID.

[00:12:25] **Trent Christopher**: And it's a unique ID for the contacts that are in Quo.

[00:12:31] **Trent Christopher**: Yep.

[00:12:32] **Trent Christopher**: Okay.

[00:12:32] **Trent Christopher**: So it has that.

[00:12:35] **Trent Christopher**: And then we have jobber and then we have the content inside of the conversation that they could use for all for contact blending and enrichment.

[00:12:45] **Matthew Kerns**: Right.

[00:12:46] **Matthew Kerns**: Okay.

[00:12:48] **Trent Christopher**: I'm in order of preference.

[00:12:51] **Trent Christopher**: Jobber is priority.

[00:12:53] **Trent Christopher**: Then Quo.

[00:12:54] **Trent Christopher**: Then conversation.

[00:12:58] **Trent Christopher**: And.

[00:14:00] **Trent Christopher**: It takes two minutes because of the API, you've to wait in between calls and API and all that crap.

[00:14:08] **Trent Christopher**: Yeah.

[00:14:08] **Trent Christopher**: Two minutes to go get all of his contacts and bring them into a data table inside of N8N.

[00:14:15] **Trent Christopher**: So now all the contacts are in that table so that when we receive a call, we can do a quick lookup by phone number.

[00:14:26] **Matthew Kerns**: Okay.

[00:14:27] **Matthew Kerns**: Okay.

[00:14:28] **Matthew Kerns**: So now it makes sense to grab everything instead of listening to every update, I think.

[00:14:34] **Trent Christopher**: Well, so here's the problem that I had, okay?

[00:14:37] **Trent Christopher**: Like even if we listen to the updates, like we're only going to get the updates.

[00:14:43] **Matthew Kerns**: Yeah, right.

[00:14:44] **Matthew Kerns**: Because you're not able to search for that contact to see who was before.

[00:14:49] **Matthew Kerns**: Or could you, if we have a copy of the contact and the contact ID, and we have an update incoming web book that then.

[00:14:59] **Matthew Kerns**: if that, Yeah.

[00:15:00] **Matthew Kerns**: Would that have the contact ID and we could could we make an update that way or what's the problem happening?

[00:15:04] **Matthew Kerns**: That's exactly what's happening.

[00:15:06] **Trent Christopher**: So I have so we have contact synchronization.

[00:15:10] **Trent Christopher**: Okay, so contact synchronization happens like this.

[00:15:13] **Trent Christopher**: Here, I'm gonna pull another window in here.

[00:15:20] **Matthew Kerns**: So this is it.

[00:15:23] **Trent Christopher**: We'll get into the workflow architecture.

[00:15:43] **Trent Christopher**: Yeah, so actually, I think that this isn't everything.

[00:15:49] **Trent Christopher**: Let me look at the other one.

[00:15:50] **Trent Christopher**: There's another diagram here.

[00:15:55] **Matthew Kerns**: Diagrams are awesome.

[00:15:56] **Trent Christopher**: I know.

[00:15:57] **Trent Christopher**: They are awesome.

[00:15:58] **Trent Christopher**: I'm a visual person.

[00:15:59] **Trent Christopher**: So know, you know, know,

[00:16:00] **Trent Christopher**: Okay, so this one here is more descriptive at a high level of how things work.

[00:16:16] **Trent Christopher**: So, Quo sends us the call completed, and then we get, it's actually not call completed, it's a transcript complete, I don't know, maybe it is call completed.

[00:16:28] **Trent Christopher**: I don't know, anyway, you get a transcript, comes in, it gets processed at a Quo webhook router, all right?

[00:16:36] **Trent Christopher**: So, if the contact gets updated, it goes here to a separate webhook and gets updated to data storage.

[00:16:44] **Trent Christopher**: So, let's just, does it show sync?

[00:16:47] **Trent Christopher**: Oh, the arrow doesn't show here.

[00:16:52] **Trent Christopher**: Okay, well, that's not the ideal way, I should have Claude do that.

[00:16:59] **Trent Christopher**: But, yeah.

[00:17:00] **Trent Christopher**: So contact syncing is scheduled at 2 a.m.

[00:17:02] **Trent Christopher**: every night, it will go out, it deletes the whole table, and it goes and it gets all of the contacts and it synchronizes it to the data table, this data storage here, every night at 2 a.m.

[00:17:16] **Trent Christopher**: And we do that because I want to make sure that if for any reason that table gets out of whack, we have the latest information.

[00:17:24] **Trent Christopher**: I don't know, I don't have any control over when the iPhone syncs or what happens with Quo and all that crap.

[00:17:32] **Trent Christopher**: So let's just refresh it every night at 2 a.m.

[00:17:35] **Trent Christopher**: and then that'll keep it in sync.

[00:17:39] **Trent Christopher**: But then if a new contact or a contact gets updated, added, deleted, it comes in through this webhook and then it gets passed through and it updates the storage.

[00:17:51] **Trent Christopher**: Whether that be those different things, they can be an update, an insert, or a delete, okay?

[00:17:57] **Matthew Kerns**: So CRUD functions.

[00:17:59] **Trent Christopher**: Actually, we're not even...

[00:18:00] **Trent Christopher**: And looking it up.

[00:18:01] **Trent Christopher**: So not in that case.

[00:18:03] **Trent Christopher**: So, all right.

[00:18:04] **Matthew Kerns**: This is our copy of the data of the contacts, right?

[00:18:09] **Matthew Kerns**: So Quo itself is handling its own.

[00:18:12] **Matthew Kerns**: Okay.

[00:18:13] **Matthew Kerns**: Got it.

[00:18:14] **Matthew Kerns**: Yep.

[00:18:14] **Trent Christopher**: So Quo has a list of the contacts.

[00:18:16] **Trent Christopher**: There's nothing in the API to search it.

[00:18:18] **Trent Christopher**: So this is my solution.

[00:18:26] **Trent Christopher**: I think I'm going down.

[00:18:29] **Trent Christopher**: Okay.

[00:18:31] **Trent Christopher**: So, all right.

[00:18:34] **Trent Christopher**: So then it goes to processing.

[00:18:36] **Trent Christopher**: So it gets parsed and they're detecting, I'm detecting if it's a band.

[00:18:42] **Trent Christopher**: So there are times that there's like a four second call, like somebody calls and then they don't even want to leave a voicemail.

[00:18:49] **Trent Christopher**: So then they just hang up the phone.

[00:18:50] **Trent Christopher**: There's no reason that those let's not put the garbage in job or for stuff like that.

[00:18:56] **Trent Christopher**: So it's filtering out based on abandonment.

[00:18:59] **Trent Christopher**: Okay.

[00:18:59] **Trent Christopher**: So.

[00:18:59] **Trent Christopher**: I'm

[00:19:01] **Trent Christopher**: Content summarizer.

[00:19:03] **Trent Christopher**: So it right here is summarizing and extracting details, including caller name, identify equipment, classify request type, that kind of stuff.

[00:19:12] **Trent Christopher**: It's way more extensive than this three item thing, but it summarized it.

[00:19:17] **Trent Christopher**: So then it goes to the contact enricher.

[00:19:20] **Trent Christopher**: The purpose of the contact enricher is to combine contact info.

[00:19:26] **Trent Christopher**: OK, so it's just it's merging quo and AI data, validating names.

[00:19:33] **Trent Christopher**: OK, it's it pulls out of this database here, so it gets the quo contact.

[00:19:40] **Trent Christopher**: Because what you get on the webhook is just a contact ID.

[00:19:43] **Trent Christopher**: It doesn't really tell you anything other than an ID and a phone number.

[00:19:47] **Trent Christopher**: But you don't know any contact details like people, like the names of the company or anything.

[00:19:52] **Trent Christopher**: So that's where we get this data storage.

[00:19:54] **Trent Christopher**: That's just so that we have a way to look it up.

[00:19:58] **Trent Christopher**: All right.

[00:19:58] **Trent Christopher**: So then if.

[00:20:02] **Matthew Kerns**: No, was just saying, okay, I think I get it.

[00:20:05] **Matthew Kerns**: So you're saying on the webhook that just the client ID comes in?

[00:20:09] **Matthew Kerns**: Contact ID?

[00:20:10] **Matthew Kerns**: The contact ID.

[00:20:11] **Trent Christopher**: It's like a unique ID.

[00:20:12] **Trent Christopher**: It's like alphanumeric.

[00:20:13] **Matthew Kerns**: Yep.

[00:20:14] **Matthew Kerns**: Okay.

[00:20:14] **Matthew Kerns**: So you get the metadata from our storage, which we're managing those to keep it as updated as possible.

[00:20:21] **Matthew Kerns**: Yep, yep, yep.

[00:20:22] **Trent Christopher**: So once we take that, okay, there is also the possibility that when you have internal calls, or when you have, it's using this client fuzzy matcher to, if names are spelled slightly different in the transcript, it will try to identify that particular contact in the search to data storage.

[00:20:51] **Trent Christopher**: Okay.

[00:20:52] **Trent Christopher**: You where it says like confidence scoring and name-based search and identifying internal calls.

[00:20:59] **Trent Christopher**: specified what says.

[00:20:59] **Trent Christopher**: Yep.

[00:20:59] **Trent Christopher**: Yeah.

[00:20:59] **Trent Christopher**: I'm

[00:21:00] **Matthew Kerns**: And now it's checking Jobber for Jobber contacts?

[00:21:05] **Trent Christopher**: Yeah, it's trying to match the Jobber contact.

[00:21:08] **Trent Christopher**: It didn't link it here, but it's checking Jobber and it's comparing our contact details that we retrieved over our pipeline.

[00:21:18] **Trent Christopher**: It's comparing Jobber to what we have.

[00:21:22] **Trent Christopher**: It's preferring Jobber.

[00:21:27] **Trent Christopher**: But there's the possibility, for example, that REID, for example, let me see if it's in the Jobber here.

[00:21:41] **Trent Christopher**: Just show you down here if there's a REID.

[00:21:44] **Trent Christopher**: Yeah, so REID.

[00:21:45] **Trent Christopher**: So REID, okay?

[00:21:49] **Trent Christopher**: This is an actual contact, but if you were to read the request details, you'll see this.

[00:21:58] **Matthew Kerns**: Yeah.

[00:21:59] **Matthew Kerns**: Yeah.

[00:21:59] **Matthew Kerns**: Thank you.

[00:22:00] **Matthew Kerns**: That's how it was transcribed.

[00:22:02] **Trent Christopher**: So that's the purpose of the fuzzy matcher is that if you don't have a, you have to make sure that you're not creating a new contact that just because it misspelled the name, right?

[00:22:12] **Trent Christopher**: Yeah.

[00:22:13] **Matthew Kerns**: A hundred percent.

[00:22:14] **Matthew Kerns**: That's good.

[00:22:15] **Matthew Kerns**: Yeah.

[00:22:15] **Matthew Kerns**: Yeah.

[00:22:16] **Trent Christopher**: So, okay.

[00:22:17] **Trent Christopher**: So then coming back to this, um, it creates a new client with all the information that we've retrieved here.

[00:22:27] **Trent Christopher**: It prefers jobber information.

[00:22:30] **Trent Christopher**: So it won't, it's not going to overwrite what's in jobber.

[00:22:34] **Trent Christopher**: It's just going to prefer whatever's there.

[00:22:37] **Trent Christopher**: Okay.

[00:22:40] **Trent Christopher**: Right.

[00:22:42] **Trent Christopher**: And then it will create a new request because it's a new client anyway, but then the jobber request manager handles if it's a new request or if it's a request that needs to have the note appended.

[00:22:56] **Trent Christopher**: Okay.

[00:22:58] **Trent Christopher**: Okay.

[00:23:00] **Matthew Kerns**: So that's that's kind of like the whole flow of things.

[00:23:05] **Trent Christopher**: We can look more at the details of what's in Java.

[00:23:12] **Chris Andrade**: My guys, what up, my dudes?

[00:23:14] **Chris Andrade**: What up, what up, what up?

[00:23:16] **Chris Andrade**: Sorry, man.

[00:23:17] **Chris Andrade**: It's all good.

[00:23:19] **Trent Christopher**: So let's look here at Max.

[00:23:22] **Trent Christopher**: So Max, this is a phone call.

[00:23:24] **Trent Christopher**: This one here doesn't really have much.

[00:23:26] **Trent Christopher**: It says it was between.

[00:23:27] **Trent Christopher**: Oh, this is a Verizon call.

[00:23:28] **Trent Christopher**: So this is a call that Kelsey was making to Verizon.

[00:23:34] **Trent Christopher**: Yep.

[00:23:34] **Trent Christopher**: OK, so it's not really relevant.

[00:23:37] **Trent Christopher**: And in this case, Alyssa would take it and just delete it.

[00:23:41] **Trent Christopher**: There's no reason to keep it.

[00:23:43] **Trent Christopher**: Yep.

[00:23:44] **Trent Christopher**: Right.

[00:23:45] **Trent Christopher**: So and that's something that like we can work on to try to dial it in a little better.

[00:23:49] **Trent Christopher**: But I'm I'm more worried about making sure we capture things and let humans evaluate it than I am the AI potentially making a mistake and pitching things that it shouldn't be.

[00:23:59] **Trent Christopher**: next Bye.

[00:23:59] **Trent Christopher**: Thank

[00:24:00] **Trent Christopher**: Yeah, 100% agree.

[00:24:02] **Matthew Kerns**: That's good.

[00:24:02] **Matthew Kerns**: It seems to have handled it pretty well.

[00:24:05] **Matthew Kerns**: Like I said, none, no actions, no equipment mentioned, no equipment issues.

[00:24:11] **Matthew Kerns**: Even though it's like a phone, it's like they are discussing an issue, but it's not printer related.

[00:24:17] **Matthew Kerns**: So it seems like it's a good job.

[00:24:19] **Trent Christopher**: It did a pretty good job.

[00:24:20] **Trent Christopher**: Yeah.

[00:24:21] **Trent Christopher**: So this one here is talking about a Dropbox issue.

[00:24:25] **Trent Christopher**: This is Chris.

[00:24:26] **Trent Christopher**: Okay.

[00:24:28] **Trent Christopher**: So, but here's the contact, the contact info.

[00:24:31] **Trent Christopher**: It created this.

[00:24:33] **Trent Christopher**: It created it based on the Quo contact.

[00:24:35] **Trent Christopher**: So whatever, whatever came in through Quo.

[00:24:40] **Chris Andrade**: Yeah.

[00:24:44] **Matthew Kerns**: That's actually Chris's middle name.

[00:24:50] **Chris Andrade**: Oh yeah.

[00:24:52] **Chris Andrade**: Yeah.

[00:24:53] **Chris Andrade**: I'm going to put it on my birth certificate.

[00:24:55] **Chris Andrade**: There you go.

[00:24:56] **Chris Andrade**: There we go.

[00:24:57] **Trent Christopher**: I'm looking at John.

[00:25:00] **Trent Christopher**: So here's John's call, Epson R5070.

[00:25:05] **Trent Christopher**: So the next steps is John is going to send a picture of the parts to Kelsey or Dan's email.

[00:25:10] **Trent Christopher**: John will keep Potter mechanics in the loop about, I don't know who Dan is, but Potter mechanics will coordinate with Dan.

[00:25:18] **Trent Christopher**: So Dan must be somebody related to John.

[00:25:24] **Trent Christopher**: I don't know who Dan and John is.

[00:25:26] **Trent Christopher**: They must be part of the same company or something.

[00:25:31] **Trent Christopher**: So equipment mentioned, right?

[00:25:33] **Trent Christopher**: It's got a resin printer, latex 570s, a Canon printer, equipment issues.

[00:25:38] **Trent Christopher**: This one has a printhead, potentially needs replacement.

[00:25:41] **Trent Christopher**: This one here's print quality issues.

[00:25:44] **Trent Christopher**: one here's Epson left a pile of parts, printheads, purge units, all kinds of .

[00:25:51] **Chris Andrade**: Yeah.

[00:25:51] **Chris Andrade**: Plotter mechanics instructions.

[00:25:53] **Chris Andrade**: They need to offer expertise in the printhead replacement.

[00:25:56] **Trent Christopher**: They need to send the pictures of the parts to Kelsey or Dan's email.

[00:26:01] **Trent Christopher**: Key plotter mechanics in the loop about John.

[00:26:04] **Trent Christopher**: He's definitely planning on heading up.

[00:26:07] **Trent Christopher**: And it picked out John, Grow Digital Gear, Northern Arizona, and these numbers.

[00:26:17] **Chris Andrade**: Sorry, I don't mean to interrupt.

[00:26:20] **Chris Andrade**: We also not only need to start, same thing with S&S, geographical location.

[00:26:26] **Chris Andrade**: How hard is it to incorporate Google Earth?

[00:26:31] **Chris Andrade**: Not.

[00:26:32] **Chris Andrade**: There's an API for it.

[00:26:34] **Chris Andrade**: Where they can not only see the client, or get the client, but see where they are at physically on the road.

[00:26:44] **Chris Andrade**: That would next level it up when we consolidate all his contacts, because that's what he's needing.

[00:26:50] **Chris Andrade**: We're going to have, that's going to be a whole process of, like, someone's going to have to get paid for that, right?

[00:26:56] **Chris Andrade**: Because, from what I gathered this morning.

[00:27:00] **Chris Andrade**: Trent, how vast the layers of contacts that has to be consolidated to go through to bring to one is a lot, and then the second component that Kelsey needs to incorporate now is not only the contact, but the equipment, the model, the serial to develop the service plans.

[00:27:34] **Trent Christopher**: So this call here, customer Kimberly at APS, so we can see that the AI summarized it using the transcript from APS, but if we look at the contact, what we'll see is that it says APS Flagstaff, well, that came from Quo contacts, because Amy's in, or this says Kimberly,

[00:28:00] **Trent Christopher**: Okay.

[00:28:04] **Chris Andrade**: Kimberly was this phone number.

[00:28:08] **Trent Christopher**: We're looking up contact details by phone number because that's the most reliable way to look up contacts.

[00:28:15] **Trent Christopher**: That's the way almost all contact solutions do it.

[00:28:19] **Chris Andrade**: So can we make another note that if we can start associating, there's three zip codes.

[00:28:25] **Chris Andrade**: 602, 623, and 480 are with Phoenix Metropolitan.

[00:28:35] **Chris Andrade**: 520 is Tucson.

[00:28:37] **Chris Andrade**: 928 is Flagstaff in Northern Arizona.

[00:28:41] **Chris Andrade**: Yeah, can.

[00:28:42] **Trent Christopher**: Yeah, can.

[00:28:42] **Trent Christopher**: Once we get into the application there, we can figure that out.

[00:28:45] **Trent Christopher**: But so here.

[00:28:47] **Trent Christopher**: So this one right here, Kelsey from Plotter Mechanics is on a call with a customer running a Canon TM305 with a system error code.

[00:28:55] **Trent Christopher**: Kelsey, customer troubleshoot the issue.

[00:28:58] **Trent Christopher**: There's the equipment mentioned.

[00:28:59] **Trent Christopher**: time.

[00:29:00] **Trent Christopher**: And next steps are Kelsey's to go to Kingman, and Joe or Kelsey to pick up parts.

[00:29:06] **Trent Christopher**: Here's Potter mechanics instructions suggesting that Kelsey go to Kingman to troubleshoot, Joe and or Kelsey grab parts from the person on Monday.

[00:29:16] **Chris Andrade**: That's what's coming from would be a opposing tactic, because he's taking, dude, that's like a huge drive, like round trip, that's like 600 miles.

[00:29:26] **Chris Andrade**: And if there was a way that he can make a stop in Flagstaff, just to say, hey, what up?

[00:29:31] **Chris Andrade**: Oh, hey, I know you're going to need this.

[00:29:33] **Chris Andrade**: I just wanted, I'm on my way.

[00:29:35] **Chris Andrade**: Drop this off real quick.

[00:29:37] **Chris Andrade**: Yep.

[00:29:37] **Chris Andrade**: Yep.

[00:29:38] **Matthew Kerns**: So supplies details.

[00:29:39] **Trent Christopher**: We got like, it must've been mentioned in the conversation, an encoder unit, paper feed motor and a disc.

[00:29:46] **Trent Christopher**: Those must've been mentioned in the conversation.

[00:29:48] **Trent Christopher**: So.

[00:29:49] **Trent Christopher**: Yeah.

[00:29:50] **Matthew Kerns**: We're part of the SOP where, because we're going to provide them with SOPs.

[00:29:55] **Matthew Kerns**: How to ideally use this stuff so we can say like, make sure you.

[00:30:00] **Matthew Kerns**: You get important information about the location in the conversation.

[00:30:04] **Matthew Kerns**: Like, do you just need city?

[00:30:06] **Matthew Kerns**: Do you need address?

[00:30:08] **Matthew Kerns**: Like, should we tell them to get the address, I wonder, in the SOP?

[00:30:13] **Matthew Kerns**: I don't know.

[00:30:14] **Trent Christopher**: What do you mean?

[00:30:15] **Trent Christopher**: Like, how are they going to get the address?

[00:30:17] **Matthew Kerns**: Like, how do they know where to go for a service call?

[00:30:22] **Matthew Kerns**: Should we have them talk about it on the phone, and then it gets fed through here, and then that's how they know?

[00:30:27] **Matthew Kerns**: Yeah, if they dictate it well enough, it'll be accurate.

[00:30:31] **Trent Christopher**: So one of the problems they have right now, Kelsey even talked about, was that some of those contacts, there's an address related to it, but that doesn't necessarily mean that's where the service location is.

[00:30:44] **Trent Christopher**: Right.

[00:30:45] **Trent Christopher**: So what Alyssa has been doing is she will copy and paste, like, the person, the phone number, and the location, and she puts it in the notes.

[00:30:58] **Trent Christopher**: She sends it to She's sending it to me.

[00:30:59] **Trent Christopher**: me.

[00:31:00] **Trent Christopher**: just to make sure that everything's accurate.

[00:31:02] **Trent Christopher**: So he has quick access to it.

[00:31:04] **Matthew Kerns**: Where is she copy and pasting that from?

[00:31:07] **Trent Christopher**: I don't think she's copying.

[00:31:08] **Trent Christopher**: I don't know if she's copying and pasting it or from an email or she's got notes that she's writing down or whatever she's doing because she's literally putting it in a field.

[00:31:16] **Trent Christopher**: She's putting in a field that's just blank.

[00:31:19] **Matthew Kerns**: Yeah.

[00:31:19] **Matthew Kerns**: Oh, so it doesn't even say service location field.

[00:31:23] **Trent Christopher**: No, there's no fields.

[00:31:24] **Trent Christopher**: It's just notes.

[00:31:25] **Trent Christopher**: Like you just add note right here and type it.

[00:31:29] **Matthew Kerns**: Yeah.

[00:31:29] **Matthew Kerns**: Yeah.

[00:31:30] **Matthew Kerns**: But okay.

[00:31:31] **Matthew Kerns**: But at some point in their current process, they must be like, okay, where are we going for this service?

[00:31:36] **Matthew Kerns**: Yeah.

[00:31:37] **Matthew Kerns**: What's the address?

[00:31:38] **Trent Christopher**: So one of the things we're going to have to make sure we do with the SOP is that especially right now, and we're going to be in a building trust phase.

[00:31:47] **Trent Christopher**: Okay.

[00:31:47] **Trent Christopher**: So Alyssa, even though we're helping her by giving her details, she's going to have to back check this stuff, like sort of in a way like she used to do, she has to, she has to make sure she has the correct information.

[00:32:00] **Trent Christopher**: And she has to make sure that the information from the A.I.

[00:32:03] **Trent Christopher**: is correct.

[00:32:05] **Trent Christopher**: She has to do that anyway now.

[00:32:07] **Trent Christopher**: She just has to do it so we can build trust.

[00:32:10] **Trent Christopher**: Right.

[00:32:12] **Matthew Kerns**: And note down times where it was incorrect.

[00:32:16] **Matthew Kerns**: Like for a whole week, where was it incorrect?

[00:32:18] **Matthew Kerns**: Yeah, we need to know.

[00:32:20] **Trent Christopher**: Is there any flaws in what she received?

[00:32:23] **Trent Christopher**: Yeah, because we can make it better.

[00:32:24] **Trent Christopher**: And the more detail she can provide us, the better.

[00:32:28] **Trent Christopher**: But we don't want to bog her down and slow her down.

[00:32:30] **Trent Christopher**: We want to speed her up.

[00:32:31] **Trent Christopher**: So it's things she observes along her path.

[00:32:34] **Trent Christopher**: She needs to find a quick way to be able to tell us that there's an issue.

[00:32:39] **Chris Andrade**: So there's a there's a really cool feature that I like on this camera where I can click a button and it will straight shine down straight on my desk.

[00:32:48] **Chris Andrade**: And because the way she operates, I feel if we had a camera that can just kind of just communicate, we can communicate not only to her, but the whole office.

[00:32:58] **Chris Andrade**: Yeah, I mean.

[00:32:59] **Chris Andrade**: mean.

[00:32:59] **Chris Andrade**: Thank you.

[00:33:00] **Trent Christopher**: Sure, but I'm not sure that that provides us a lot of value with this instance.

[00:33:05] **Trent Christopher**: The reason I say that is that if we can get her to use like a screenshot app, or she can just copy and paste the note, or she can just write down like the name and the date and time or something, like she could literally just take this right here and copy this and paste that into a note.

[00:33:24] **Chris Andrade**: So Chip was just talking about this, he just rolled this out as his standard operational practice.

[00:33:32] **Chris Andrade**: I'm uploading that to the audios right now.

[00:33:35] **Chris Andrade**: Apparently, Microsoft or Windows has this new feature with AI, but he uses this app to screen record his daily task.

[00:33:45] **Chris Andrade**: So as they're operating and going in and out of systems, it's being recorded.

[00:33:51] **Chris Andrade**: So then it gives them a daily summary on their whole environments of where they went in, how they walked.

[00:34:00] **Chris Andrade**: What they did, when they did it, in case something happened, they knew exactly where to go to get it, to break.

[00:34:10] **Chris Andrade**: That reminds me of what I'm doing with Loom.

[00:34:14] **Matthew Kerns**: Yeah, that is the next level and that's going to be huge for when we're leveling up our audit game for figuring out where people actually spend their time.

[00:34:23] **Matthew Kerns**: Yep.

[00:34:25] **Matthew Kerns**: Yeah, yeah, exactly.

[00:34:26] **Trent Christopher**: So it created Vince CES Service Manager.

[00:34:29] **Trent Christopher**: So note here that Vince CES Service Manager is the contact name in Kelsey's phone.

[00:34:36] **Trent Christopher**: So, right.

[00:34:38] **Trent Christopher**: But you can see here that there's an email, Dana Patterson.

[00:34:43] **Trent Christopher**: So like, but look here, look at all the contact info that came in.

[00:34:49] **Trent Christopher**: Yep.

[00:34:49] **Trent Christopher**: Okay.

[00:34:50] **Trent Christopher**: So it got all the emails and addresses from the Quo contact.

[00:34:57] **Trent Christopher**: So what are you wanting to do?

[00:34:59] **Chris Andrade**: What's your name?

[00:35:00] **Chris Andrade**: Nice plan, Mike, with all this craziness.

[00:35:02] **Chris Andrade**: Well, to switch it on.

[00:35:05] **Matthew Kerns**: Oh, so right now, Trent is going over all the details of the current state of the integration with me so that we can be on the same page and we can figure out what is our, is it ready right now to switch it over, to switch it on?

[00:35:23] **Matthew Kerns**: Or what do we need to make sure is good before we do that?

[00:35:30] **Chris Andrade**: Yeah, and I can switch it on and then switch it off quickly, so it's not.

[00:35:34] **Chris Andrade**: What do you mean by switch it, I guess I'm confused about what you mean by switch it on.

[00:35:39] **Trent Christopher**: So, okay, so the current state of things with Plotter Mechanics Quo and Jobber integration is it's literally just the built-in Quo to Jobber integration.

[00:35:53] **Trent Christopher**: Like, so nothing that I'm doing right now is actually being applied to their current system.

[00:35:58] **Trent Christopher**: What I'm showing you right now.

[00:36:00] **Trent Christopher**: It's my demo environment.

[00:36:03] **Chris Andrade**: Oh, .

[00:36:05] **Chris Andrade**: Yeah.

[00:36:05] **Trent Christopher**: So this is the stuff that I've been working on.

[00:36:09] **Trent Christopher**: And what looks like, yeah, this is stuff I'm working on.

[00:36:13] **Trent Christopher**: So this is, this is stuff that hasn't even been implemented for Chelsea.

[00:36:17] **Trent Christopher**: Does Chelsea even know about any of this?

[00:36:20] **Chris Andrade**: He does.

[00:36:21] **Trent Christopher**: I've given him screenshots.

[00:36:23] **Chris Andrade**: Oh.

[00:36:24] **Chris Andrade**: To get his feedback on it.

[00:36:25] **Trent Christopher**: Just a little bit.

[00:36:25] **Trent Christopher**: I just send him like a little teaser.

[00:36:26] **Trent Christopher**: Like, hey, this is what I'm working on.

[00:36:28] **Trent Christopher**: How's it look?

[00:36:29] **Chris Andrade**: And that's when he gets all fired up, huh?

[00:36:32] **Chris Andrade**: That's what you get.

[00:36:33] **Chris Andrade**: So you get them all , you get that.

[00:36:35] **Chris Andrade**: Okay.

[00:36:35] **Chris Andrade**: Now it's starting to make sense.

[00:36:37] **Chris Andrade**: Because I've been wondering, I've been seeing like, he gets all crazy fired up.

[00:36:42] **Chris Andrade**: And now it makes sense.

[00:36:43] **Chris Andrade**: I'm like, okay, now I get it.

[00:36:46] **Chris Andrade**: This is flowing.

[00:36:48] **Chris Andrade**: Perfect.

[00:36:48] **Chris Andrade**: correlated with the times that Trent texts him.

[00:36:52] **Matthew Kerns**: Yeah.

[00:36:53] **Trent Christopher**: The phone calls that you're getting are probably correlated with text messages from me.

[00:36:57] **Trent Christopher**: Yeah.

[00:36:58] **Trent Christopher**: That is so f***ing.

[00:36:59] **Chris Andrade**: f***ing.

[00:37:00] **Chris Andrade**: That's freaking, this is what I love.

[00:37:02] **Chris Andrade**: I really love this new platform, this time management stuff, and we call it the end of the week.

[00:37:07] **Chris Andrade**: It's so cool.

[00:37:09] **Chris Andrade**: It's called Friday Wrap Ups.

[00:37:11] **Chris Andrade**: Yeah, pretty cool.

[00:37:13] **Trent Christopher**: Yeah, so here's, here's what Quo integration with Jobber looks like.

[00:37:17] **Trent Christopher**: Okay, it just comes in as a phone number, it says new call, just these top two here.

[00:37:22] **Trent Christopher**: Okay.

[00:37:23] **Trent Christopher**: And when I grab it, and I look at it, here's what you get from Quo.

[00:37:29] **Trent Christopher**: You have a new contact with a phone number, you have a summary, you have next steps.

[00:37:35] **Trent Christopher**: Okay?

[00:37:36] **Trent Christopher**: Okay.

[00:37:37] **Trent Christopher**: You have a transcript from the right.

[00:37:39] **Chris Andrade**: When you want to say turn it on and turn it off, right?

[00:37:42] **Chris Andrade**: When you say we can turn it on real fast and turn it off.

[00:37:45] **Chris Andrade**: When we turn it on, it would, I would imagine there'd be like, we're doing like a stress test, right?

[00:37:54] **Chris Andrade**: The stress test is going to be real world.

[00:37:58] **Trent Christopher**: Okay.

[00:37:59] **Trent Christopher**: I've been stressed.

[00:37:59] **Chris Andrade**: stressed.

[00:37:59] **Chris Andrade**: The stress

[00:38:00] **Trent Christopher**: We testing it with real-world data, but it's not connected to their Java.

[00:38:04] **Chris Andrade**: Okay, so then what is, so if there was an emergency, like when I studied cybersecurity, right, and there were protocols when rollouts happened, and what I gathered, like with the NIST 2, right, is that you had to have a backup plan, right?

[00:38:23] **Chris Andrade**: What is that backup plan?

[00:38:27] **Chris Andrade**: It's to turn it off.

[00:38:29] **Trent Christopher**: And how do you turn that off?

[00:38:31] **Chris Andrade**: Is it literally by a flick of a switch?

[00:38:33] **Chris Andrade**: I mean, pretty much.

[00:38:34] **Trent Christopher**: I can just turn it off.

[00:38:36] **Chris Andrade**: So you're going to be like, oh, I'm not getting any phone calls, Trent, and we're like, oh, okay, off, and it plugs it right back?

[00:38:44] **Chris Andrade**: Yeah, I mean, pretty much.

[00:38:46] **Matthew Kerns**: That's a great question, and that's because that's like, yeah, what's our rollback plan?

[00:38:51] **Matthew Kerns**: If we turn it off, does the quota Java integration automatically re-enable?

[00:38:57] **Matthew Kerns**: No.

[00:38:58] **Matthew Kerns**: So we have to...

[00:38:59] **Matthew Kerns**: That would be...

[00:39:00] **Matthew Kerns**: Yeah, two-step thing.

[00:39:01] **Trent Christopher**: would turn off mine and I would turn on theirs.

[00:39:03] **Matthew Kerns**: Okay, so we need to have that documented, I would say, like, in a Notion document somewhere?

[00:39:11] **Matthew Kerns**: Yeah, sure.

[00:39:13] **Chris Andrade**: Because ultimately, why we want that is to make them aware, hey, this is what our plan is.

[00:39:19] **Chris Andrade**: And then if it does happen where  doesn't go through, excuse my language, then we need to, this is our backup plan.

[00:39:28] **Chris Andrade**: And I think if we just illustrate that, it alleviates the worry a little bit, you know what I'm saying?

[00:39:35] **Chris Andrade**: Yeah.

[00:39:36] **Trent Christopher**: So, if you look here, after I've gone through all these, we have Kelsey, okay?

[00:39:42] **Trent Christopher**: This is a call, did it not mark it internal?

[00:39:47] **Trent Christopher**: Hold on, this is a call, phone call with Kelsey.

[00:39:54] **Trent Christopher**: Call was initiated by Plotter Mechanics staff to return a missed call, Vince.

[00:39:59] **Trent Christopher**: questions.

[00:39:59] **Trent Christopher**: next started.

[00:39:59] **Trent Christopher**: No

[00:40:00] **Trent Christopher**: Trying to reach the owner, Vince stated they would call back on Monday.

[00:40:05] **Trent Christopher**: So this might not be accurate.

[00:40:08] **Chris Andrade**: Hey Trent, I'm seeing what I'm looking at and like, I'm just making my mind go crazy.

[00:40:14] **Chris Andrade**: Real quick, my penalty is convinced that he needs this maker and manager mindset as well.

[00:40:23] **Chris Andrade**: Is there a way we can incorporate a little side agent to adopt that and really start delegating tasks for Kelsey on the side?

[00:40:35] **Trent Christopher**: I mean, there's methodology that we can help him with, sure, but that's not like, it's not in our scope currently, right?

[00:40:42] **Trent Christopher**: And we don't even have it figured out ourselves.

[00:40:44] **Chris Andrade**: Yeah, that's why I spent a lot of my time today and last night in trying to really figure out how to like, build and help create your ego system, my friend, because dude, I want to sell that .

[00:40:59] **Chris Andrade**: sorry get it.

[00:41:01] **Matthew Kerns**: So I think, yes, and it's a highly valuable thing, but we need to make sure that's Phase 2, and right now we're trying to finish up Phase 1 on this call.

[00:41:13] **Matthew Kerns**: No, I get it.

[00:41:14] **Matthew Kerns**: guess, again, you know how I think.

[00:41:16] **Chris Andrade**: I'm sorry.

[00:41:17] **Chris Andrade**: Yeah, I don't want to be a dick, but I'm sorry too.

[00:41:21] **Matthew Kerns**: Yeah, yeah.

[00:41:22] **Trent Christopher**: So one thing, I'm looking at this call though, and I'm wondering, I tried to handle this at one point in time, and I don't know what the outcome was.

[00:41:33] **Trent Christopher**: Vince was mentioned in the call.

[00:41:36] **Trent Christopher**: It was 20 seconds long.

[00:41:39] **Trent Christopher**: Jeez.

[00:41:40] **Trent Christopher**: But Kelsey is actually the contact that was created here, which is not what I wanted, because this number is actually a quo number.

[00:41:52] **Trent Christopher**: Oh, snap.

[00:41:54] **Chris Andrade**: I see what you're saying now.

[00:41:56] **Chris Andrade**: Okay.

[00:41:57] **Chris Andrade**: So this actually shouldn't have happened, so I probably...

[00:42:00] **Trent Christopher**: We make sure that I'd fix that.

[00:42:02] **Chris Andrade**: And how, so is that like, like how, if you recorded that problem and gave it to your bot, would it help you fix it?

[00:42:13] **Chris Andrade**: Yeah, I mean, that's how I've been doing it.

[00:42:15] **Trent Christopher**: Is that once I have an issue.

[00:42:17] **Trent Christopher**: Yeah, once I have these issues, I explain it, the cloud code, and it helps me solve the problem.

[00:42:21] **Trent Christopher**: Well, it makes an attempt at solving the problem.

[00:42:24] **Trent Christopher**: So it depends on how well I describe the issue and how well it understands the issue.

[00:42:30] **Chris Andrade**: I'm starting to understand your guys'  level.

[00:42:34] **Chris Andrade**: I'm like, I'm like, I get there.

[00:42:35] **Chris Andrade**: I get it.

[00:42:36] **Chris Andrade**: Like, I just had a little scratch surface of it last night, and I'm like, oh my gosh, dude.

[00:42:43] **Chris Andrade**: It's like a drug.

[00:42:45] **Trent Christopher**: So this one here would be, is a little questionable.

[00:42:48] **Trent Christopher**: So I need to try to figure that one out.

[00:42:50] **Trent Christopher**: So can you like flag it or mark it somehow to like a questionable one?

[00:42:56] **Chris Andrade**: That's a good question, actually.

[00:42:58] **Trent Christopher**: Let's see.

[00:42:58] **Trent Christopher**: What is that?

[00:43:00] **Chris Andrade**: Like to the right, what's that marker right there with the pencil?

[00:43:03] **Chris Andrade**: What is that?

[00:43:04] **Chris Andrade**: To edit the area.

[00:43:06] **Trent Christopher**: So, for example, if I click that, lets me edit this phone call name.

[00:43:10] **Chris Andrade**: What if you just put a name in Clinch and like phone call, it's 20 seconds, and then like dash dash R or something for review?

[00:43:19] **Trent Christopher**: So that is also possible for our SOPs for Alyssa.

[00:43:27] **Chris Andrade**: Oh, for reviews, just name the convention with a certain culture, and then add it that way?

[00:43:35] **Trent Christopher**: Just edit it and just put something on here.

[00:43:38] **Trent Christopher**: Boom.

[00:43:40] **Trent Christopher**: Like an X or something.

[00:43:41] **Trent Christopher**: don't know.

[00:43:42] **Trent Christopher**: Anything.

[00:43:42] **Trent Christopher**: Yeah, yeah, perfect.

[00:43:43] **Chris Andrade**: And then we can designate that, right?

[00:43:46] **Trent Christopher**: Something that's easy for her to put in.

[00:43:48] **Trent Christopher**: Yeah, that's actually, I mean, that's, yeah.

[00:43:51] **Chris Andrade**: How did you, okay, damn, you did that so fast.

[00:43:54] **Chris Andrade**: And then she can, as you do that and then archive it.

[00:43:59] **Trent Christopher**: she archives it.

[00:44:00] **Trent Christopher**: Then we can come back to it later, okay?

[00:44:03] **Matthew Kerns**: So where do, just a quick question about archive, where do archives go for them?

[00:44:09] **Matthew Kerns**: Like we can see it in our database, right?

[00:44:11] **Matthew Kerns**: But can they see it later?

[00:44:13] **Trent Christopher**: We can't see it necessarily in our, we can see the webhook data that came through.

[00:44:21] **Trent Christopher**: Over the last 30 days, we can, we're keeping track of the webhooks that come through.

[00:44:29] **Trent Christopher**: But, okay, so let's just do this one here.

[00:44:31] **Trent Christopher**: This is Kelsey, phone call 20 seconds.

[00:44:34] **Trent Christopher**: Okay, so I'm gonna take it, I'm gonna, I'm gonna, let's just do it exactly like what we would expect her to do.

[00:44:39] **Trent Christopher**: I don't know if this is the right way or not, but I don't know if we put a star, we put an exclamation.

[00:44:45] **Trent Christopher**: Honestly, dude, what's the easiest  button to hit that we can make?

[00:44:49] **Trent Christopher**: Is she gonna use like an exclamation on anything?

[00:44:52] **Trent Christopher**: I don't think so.

[00:44:53] **Trent Christopher**: Is there a marker that we can use without having hit shift?

[00:44:59] **Chris Andrade**: Um...

[00:44:59] **Trent Christopher**: I You Pittsburgh,

[00:45:04] **Matthew Kerns**: I mean, think we need to plan it out overall, like, what are all the markers we're going to do, and then that's how we come up with a name for the extension.

[00:45:15] **Chris Andrade**: But yeah, most ideally, she wouldn't have to press shift, and it's just a quick key.

[00:45:19] **Trent Christopher**: She just clicked the pencil, she types whatever in here, and she presses save.

[00:45:24] **Trent Christopher**: But let's just, for now, let's just do this and just press save.

[00:45:27] **Trent Christopher**: She just hits the same three buttons, boom, boom, boom.

[00:45:31] **Chris Andrade**: And I'm going to do archive.

[00:45:32] **Trent Christopher**: So now it says archive the request.

[00:45:35] **Trent Christopher**: So now if I go to requests, and all these are new, new, new, new, new, new, But then the archive, it goes to the bottom.

[00:45:41] **Trent Christopher**: Okay.

[00:45:43] **Trent Christopher**: And you can filter it, so you can click here and just say archived.

[00:45:46] **Trent Christopher**: Awesome.

[00:45:47] **Chris Andrade**: Okay.

[00:45:48] **Trent Christopher**: Or you can just say, well, I want just new.

[00:45:52] **Matthew Kerns**: And we're not storing this in our database, but we have access to their jobber, so we could go in and see those.

[00:45:57] **Matthew Kerns**: Correct.

[00:45:58] **Matthew Kerns**: Yeah.

[00:45:59] **Matthew Kerns**: Cool.

[00:46:00] **Matthew Kerns**: Exactly.

[00:46:01] **Matthew Kerns**: So, yeah.

[00:46:04] **Chris Andrade**: So, all right.

[00:46:05] **Trent Christopher**: So clear filters going back to where we were at.

[00:46:08] **Trent Christopher**: So another thing to show here is that Mike and Mike, the reason there's two of them is because of the phone number, 252-4700.

[00:46:24] **Trent Christopher**: And this one here is 828-6422.

[00:46:27] **Trent Christopher**: And we probably don't have a last name.

[00:46:30] **Trent Christopher**: There's two Mikes.

[00:46:32] **Trent Christopher**: It says Arise testing is the source, but who's the contact?

[00:46:36] **Trent Christopher**: Let's see.

[00:46:38] **Chris Andrade**: Does it have location?

[00:46:39] **Chris Andrade**: It just has a number.

[00:46:40] **Trent Christopher**: It's just a phone number.

[00:46:43] **Trent Christopher**: Nothing in the context of, like, location at all?

[00:46:46] **Trent Christopher**: Mike is sending a picture of the serial number to Alyssa.

[00:46:50] **Trent Christopher**: So, what if she just puts that in the SLP?

[00:46:52] **Chris Andrade**: Just put, if that, if there's no whatever, then just put the details in the...

[00:46:58] **Chris Andrade**: Okay.

[00:46:59] **Chris Andrade**: ...

[00:46:59] **Chris Andrade**: ...

[00:47:01] **Matthew Kerns**: So that's an interesting test case because Mike, there probably would be a lot of Mikes who are, we don't, maybe we don't know their last name because it's a common name.

[00:47:12] **Matthew Kerns**: Part of the SOP might be like, when you're on the call, let's get a last name.

[00:47:16] **Matthew Kerns**: Let's get metadata.

[00:47:18] **Matthew Kerns**: Like, who's the company?

[00:47:20] **Matthew Kerns**: We don't know that.

[00:47:21] **Matthew Kerns**: We don't know location.

[00:47:22] **Matthew Kerns**: Cross streets, just even cross streets would be helpful.

[00:47:26] **Chris Andrade**: Here, I don't know if Phoenix is built on a military grid, bro.

[00:47:30] **Chris Andrade**: So everything's on cross streets.

[00:47:38] **Matthew Kerns**: So if we're going to create an SOP, we want, what's the ideal data set that we could ask for?

[00:47:47] **Matthew Kerns**: Like the company location, stuff that we already have here.

[00:47:52] **Matthew Kerns**: We want like last name, company, and location.

[00:47:55] **Matthew Kerns**: And then...

[00:47:57] **Matthew Kerns**: Do you mean like to prompt Kelsey to ask for

[00:48:00] **Matthew Kerns**: Exactly.

[00:48:01] **Matthew Kerns**: Yeah.

[00:48:02] **Matthew Kerns**: He's already been asking those questions.

[00:48:03] **Trent Christopher**: like, Hey, what do I need to ask them while we're on the call?

[00:48:07] **Trent Christopher**: He's like, can I?

[00:48:08] **Chris Andrade**: Yeah.

[00:48:09] **Chris Andrade**: Yeah.

[00:48:10] **Chris Andrade**: That's what we're doing now.

[00:48:13] **Trent Christopher**: He just has to make sure he says these things and he needs to make sure he asks them.

[00:48:17] **Chris Andrade**: Guys, we have to figure out how we're going to leverage all this and really sell this thing to his wife, which this is why I'm devoting time next week to go hang out with Kelsey.

[00:48:32] **Chris Andrade**: You'll hear the transcript, like, where he wants me to come, it's like, help him.

[00:48:38] **Chris Andrade**: So I'm actually going to church, his church tomorrow morning at six o'clock.

[00:48:42] **Chris Andrade**: That's a freaking hour drive away.

[00:48:44] **Chris Andrade**: But I, I just like, I want, I want him to feel like I'm supporting him.

[00:48:51] **Chris Andrade**: And this is the only way I know how.

[00:48:52] **Matthew Kerns**: I think also the sooner we deliver the good result, then that'll convince stakeholders.

[00:49:00] **Matthew Kerns**: I think so too.

[00:49:03] **Chris Andrade**: But yeah, so this, so this is the deliverable Mr.

[00:49:08] **Chris Andrade**: Trent is what you're ultimately alluding to.

[00:49:11] **Chris Andrade**: Yeah, yeah, yeah.

[00:49:12] **Chris Andrade**: So cool.

[00:49:13] **Chris Andrade**: So I think this is the first time that I kind of got in the run through with it.

[00:49:17] **Chris Andrade**: So thank you.

[00:49:19] **Chris Andrade**: That's  amazing bro.

[00:49:21] **Chris Andrade**: I get it.

[00:49:24] **Chris Andrade**: I get it.

[00:49:24] **Matthew Kerns**: So the SOP is part of the SOW that we promised of like, and like he's, he's doing it right now, which is perfect because there's like a test, like a real test.

[00:49:36] **Matthew Kerns**: And then if we, we got to provide documents that are like, Hey, this is how the system that we're delivering ideally should be used.

[00:49:45] **Matthew Kerns**: If you perfect call would look like this is the information that the, that's communicated in the transcript so that it gets pulled out because they're going to get working.

[00:49:54] **Matthew Kerns**: And they might forget stuff.

[00:49:56] **Matthew Kerns**: So we need to deliver that, that SOP.

[00:49:58] **Matthew Kerns**: So So

[00:50:01] **Trent Christopher**: So they tested a headset.

[00:50:04] **Trent Christopher**: So he got Alyssa a headset for the computer.

[00:50:07] **Trent Christopher**: So she may not even need a phone anymore.

[00:50:10] **Trent Christopher**: She might just literally use the computer for all.

[00:50:15] **Chris Andrade**: How much do you guys know about Google phones, like Google numbers?

[00:50:20] **Chris Andrade**: Oh, yeah.

[00:50:21] **Chris Andrade**: I mean, you can do that, too.

[00:50:22] **Trent Christopher**: mean, Google.

[00:50:23] **Chris Andrade**: It used to be back in the day was hangouts, and then I don't know what happened to hangouts.

[00:50:29] **Chris Andrade**: Because I lived and eaten and breathed off that.

[00:50:32] **Chris Andrade**: Yeah, they still have it.

[00:50:34] **Trent Christopher**: I'm trying to remember what they call it, but they still have it.

[00:50:35] **Trent Christopher**: I don't know if it would be an alternative to Google or not.

[00:50:40] **Trent Christopher**: That's actually something I didn't think about.

[00:50:43] **Trent Christopher**: But anyway, so this is their calling.

[00:50:46] **Trent Christopher**: Kelsey's personal phone called the office number, I'm guessing, and talked to Alyssa.

[00:50:53] **Trent Christopher**: And this is a call test from the computer headset feature.

[00:50:57] **Trent Christopher**: The staff tested adding people to a call.

[00:51:04] **Trent Christopher**: So they must have been talking about the Titan printer as an example of what they might be.

[00:51:10] **Trent Christopher**: It says working, but dirty.

[00:51:12] **Trent Christopher**: So I don't know.

[00:51:14] **Trent Christopher**: So anyway, tell the customer if they need parts, they can get them.

[00:51:17] **Trent Christopher**: Tell the customer they can outsource full color printing to plotter mechanics.

[00:51:20] **Trent Christopher**: So he's trying to test out the system, but he doesn't have this yet, right?

[00:51:25] **Trent Christopher**: So like, he doesn't have this feature yet.

[00:51:28] **Trent Christopher**: He's not seeing this.

[00:51:30] **Trent Christopher**: So that's something that we're going to be improving for his situation.

[00:51:33] **Trent Christopher**: But I think that this needed, this is correct though.

[00:51:38] **Trent Christopher**: Or maybe we flag it as internal somehow, knowing that it's Kelsey's personal cell phone.

[00:51:44] **Trent Christopher**: Like, or maybe they know it's internal because it's Kelsey's personal cell.

[00:51:49] **Trent Christopher**: Maybe we don't worry about it because it shows right here, Kelsey personal cell.

[00:51:54] **Trent Christopher**: You know, it's internal.

[00:51:55] **Trent Christopher**: Yeah.

[00:51:56] **Matthew Kerns**: So that's like, that's calls coming from.

[00:51:59] **Matthew Kerns**: Yeah.

[00:52:00] **Matthew Kerns**: Kelsey's personal cell to anyone in any user that's in Quo, right?

[00:52:07] **Matthew Kerns**: Like, when Alyssa signs up, the same thing will happen for calls to her.

[00:52:14] **Trent Christopher**: This phone number is his new personal cell phone number that isn't in Quo.

[00:52:20] **Trent Christopher**: Okay.

[00:52:21] **Matthew Kerns**: Yeah, right.

[00:52:24] **Matthew Kerns**: But I'm wondering, who do we need to mark as internal?

[00:52:27] **Trent Christopher**: Anybody that is inside Quo is the way I see it, currently.

[00:52:33] **Trent Christopher**: Hey, real quick, we've been talking about Alyssa a lot.

[00:52:37] **Chris Andrade**: What is Joe's, can we just give a brief, like, couple-minute description on Joe and how he's, his role's going to play and integrate with this?

[00:52:46] **Trent Christopher**: Currently, Kelsey said that Joe doesn't need Quo at all, for now.

[00:52:55] **Trent Christopher**: Okay.

[00:52:55] **Trent Christopher**: Yeah, he's saying that- Outputs of-

[00:53:00] **Chris Andrade**: How can integrate with Joe for ultimate production, you know, like, what comes out of here for Joe?

[00:53:09] **Chris Andrade**: The only thing would be a print job for Joe.

[00:53:13] **Trent Christopher**: Otherwise, it's the service calls, but he takes good notes.

[00:53:17] **Trent Christopher**: I don't know, I really feel like they're going to want to get Joe, if he's doing field service calls, they're going to want to get Joe on Quo, but Kelsey's saying no, don't worry about it right now.

[00:53:28] **Trent Christopher**: Um, because Joe doesn't actually do much on the phone.

[00:53:33] **Trent Christopher**: So he's not worried.

[00:53:35] **Trent Christopher**: He thinks it's a small percentage of their business going through Joe's phone.

[00:53:41] **Chris Andrade**: Yeah.

[00:53:42] **Trent Christopher**: So, um, so here's calls for, for now, I'm just going to leave this alone and not worry about the personal cell phone.

[00:53:49] **Trent Christopher**: The reason I'm not worried about it is because it shows Kelsey personal cell.

[00:53:53] **Trent Christopher**: Uh, um, that phone number doesn't reside from Quo.

[00:54:00] **Trent Christopher**: It's a contact in Quo, but it's not a number that is inside Quo and managed by Quo.

[00:54:10] **Trent Christopher**: So anyway, I'm not going to worry about that one.

[00:54:13] **Trent Christopher**: So now going to Tom, Tom will contact plotter mechanics with an update.

[00:54:20] **Trent Christopher**: This is following up with a customer, Tom about a cutter that was repaired, Tom is checking on the status of a large cut that will contact plotter mechanics with an update.

[00:54:31] **Trent Christopher**: Tom from Apache.

[00:54:33] **Trent Christopher**: we look at Tom and from Apache.

[00:54:42] **Trent Christopher**: So that seems to be okay to me, but it's like a brief conversation.

[00:54:48] **Trent Christopher**: What are they supposed to do, right?

[00:54:50] **Trent Christopher**: They're basically waiting on Tom to get back to them.

[00:54:53] **Trent Christopher**: Get back in touch and let them know the status of the cutter.

[00:54:57] **Trent Christopher**: So that's Joe, Tom here.

[00:54:59] **Trent Christopher**: There's going to have to.

[00:55:00] **Trent Christopher**: So be maybe a little bit of interpretation on Alyssa's part.

[00:55:05] **Trent Christopher**: Because this says plotter mechanics instructions, it says get back in touch with them and let them know the status of the cutter.

[00:55:16] **Matthew Kerns**: Yeah, it's not exactly the right direction.

[00:55:19] **Matthew Kerns**: like Tom needs to get back in touch with plotter mechanics and let them know the status of the cutter.

[00:55:24] **Matthew Kerns**: Right.

[00:55:26] **Chris Andrade**: Maybe it might be like before every day.

[00:55:31] **Chris Andrade**: Right.

[00:55:32] **Chris Andrade**: Before she leaves.

[00:55:34] **Chris Andrade**: What if we give her an SOP how to do a screen record where she's trying to just to give a summary of all of the like the ones that she realizes good, the ones that she realizes that well, that's tagging was for like if she can just do this.

[00:55:50] **Trent Christopher**: And just put something in here.

[00:55:52] **Trent Christopher**: We can come back and review it later.

[00:55:54] **Chris Andrade**: Okay.

[00:55:55] **Chris Andrade**: I don't want to make this complex.

[00:55:57] **Chris Andrade**: If we ever want, if she ever felt like.

[00:56:00] **Chris Andrade**: we gave her a way to give us input, that would be a valuable option.

[00:56:04] **Chris Andrade**: Like, hey, just so you know, if you wanted to tell us something, this is how.

[00:56:08] **Chris Andrade**: That's something we talked about earlier.

[00:56:12] **Matthew Kerns**: So we definitely don't need a report of like every time it was good.

[00:56:16] **Matthew Kerns**: But if there's things that are bad, like what I was thinking is like we can batch them or she can just write it down on a piece of paper.

[00:56:26] **Matthew Kerns**: And then at the end of every week, they just send us a list of things that they didn't like.

[00:56:32] **Matthew Kerns**: And then that week over week, they'll see as we improve things, too, they'll see like that list gets smaller and smaller in theory.

[00:56:41] **Matthew Kerns**: Oh, good idea.

[00:56:43] **Chris Andrade**: And we can track that, too, and matrix that.

[00:56:46] **Chris Andrade**: Yeah, yeah.

[00:56:47] **Trent Christopher**: So this one here is Frankie Paul.

[00:56:51] **Trent Christopher**: There's a mention of supplies.

[00:56:53] **Trent Christopher**: So it tagged it as supplies.

[00:56:56] **Trent Christopher**: And it's requesting ink bags and MS.

[00:56:59] **Trent Christopher**: let's

[00:57:01] **Trent Christopher**: The name is Gary apparently, and it's not Gary.

[00:57:05] **Trent Christopher**: So Gary must have been mentioned.

[00:57:07] **Trent Christopher**: It says, Gary is going to come to the shop to purchase the ink bag.

[00:57:10] **Trent Christopher**: But this Frankie Paul is the contact info that was in Quo for this phone number.

[00:57:24] **Matthew Kerns**: So I don't know there's much I can do about that one.

[00:57:27] **Trent Christopher**: She can edit it to Gary if she wants.

[00:57:29] **Trent Christopher**: One of the things that really sucks is that if this is wrong here, you can't, there's no way to move this note to a different contact.

[00:57:43] **Trent Christopher**: She literally has to take this information and copy it like this and create a new one with the correct contact.

[00:57:52] **Trent Christopher**: Jobber doesn't give you a way to move or merge anything.

[00:57:57] **Matthew Kerns**: Okay.

[00:58:02] **Matthew Kerns**: But their original contact is Frankie Paul.

[00:58:08] **Trent Christopher**: Well, another thing here, too, is it will prefer Jobber contact info.

[00:58:12] **Trent Christopher**: So if this would have already been in Jobber with Gary as the name, it would have kept Gary.

[00:58:20] **Trent Christopher**: It wouldn't have used Frankie Paul.

[00:58:23] **Trent Christopher**: Yeah.

[00:58:24] **Matthew Kerns**: then and then Jobber just has clients.

[00:58:28] **Matthew Kerns**: doesn't have like company versus person.

[00:58:32] **Trent Christopher**: That's not entirely true.

[00:58:34] **Trent Christopher**: So you can go to a client.

[00:58:37] **Trent Christopher**: Let's just do like Kelsey, because it's an easy one to screw up or whatever if we want to.

[00:58:46] **Trent Christopher**: So you can add by editing a contact, you can add a company name.

[00:58:55] **Trent Christopher**: Right.

[00:58:56] **Trent Christopher**: So and you can check whether or not you want the company to be the.

[00:58:59] **Trent Christopher**: Okay.

[00:59:01] **Trent Christopher**: So let's just check that we want that to be the primary name, and you can come down here, and you can add additional client details, and you can add additional contacts.

[00:59:12] **Trent Christopher**: what is this task for, Trent?

[00:59:14] **Chris Andrade**: What?

[00:59:15] **Chris Andrade**: What's this task for?

[00:59:20] **Trent Christopher**: Matthew asked about the way clients work in Jobber.

[00:59:27] **Trent Christopher**: Got it.

[00:59:28] **Trent Christopher**: Clients can be a company with multiple contacts underneath it.

[00:59:35] **Trent Christopher**: It can be.

[00:59:37] **Trent Christopher**: That is generally not how their system currently is because that is actually a feature that came up after Plotter Mechanics started using Jobber.

[00:59:47] **Trent Christopher**: So their contact situation is a bit all over the place.

[00:59:51] **Chris Andrade**: This is why we need to charge in the next phase, I think is kind of important, right, to get that list.

[00:59:59] **Chris Andrade**: next task.

[00:59:59] **Chris Andrade**: task the going that's Now I'm I'm Thank

[01:00:01] **Trent Christopher**: There's been a lot of conversation from Kelsey about his CRM capsule with having a big, long list of contacts in there.

[01:00:09] **Trent Christopher**: And he's like, well, the contacts are everywhere.

[01:00:12] **Trent Christopher**: He's like, I got them in.

[01:00:13] **Trent Christopher**: I got them in quick, right?

[01:00:14] **Chris Andrade**: got them in that.

[01:00:19] **Trent Christopher**: So, and that's why I positioned it as like a consolidation line item, right?

[01:00:24] **Chris Andrade**: We're consolidating all depending on how many channels we just come up with a tally.

[01:00:29] **Chris Andrade**: Hey, this is how much work it's going to take.

[01:00:33] **Chris Andrade**: Ultimately, present that man hour factor to it.

[01:00:37] **Chris Andrade**: And then break to our hourly rate and say, this is going to be our number to really do a thorough job.

[01:00:45] **Matthew Kerns**: Yeah, that's the key to is the, what is the actual impact of improving that versus the perceived of like frustration?

[01:00:54] **Matthew Kerns**: Like maybe it's, it's kind of frustrating, but how much time does it save them really?

[01:00:59] **Matthew Kerns**: Yeah.

[01:01:00] **Matthew Kerns**: It's kind of like, that'll be interesting to figure out.

[01:01:03] **Matthew Kerns**: Yeah.

[01:01:04] **Chris Andrade**: Well, that points back to that man-hour calculator, bro.

[01:01:09] **Trent Christopher**: So, Matthew, after seeing all of these things, do you want to see anything in N8N, or do you have any questions, thoughts right now on what we need to do to make sure this is ready to turn on?

[01:01:24] **Chris Andrade**: Yeah.

[01:01:29] **Matthew Kerns**: I don't like this.

[01:01:31] **Trent Christopher**: So this is the, this is one thing I don't like, but other than that, what are, what are we thinking?

[01:01:40] **Matthew Kerns**: I'm thinking that, like, here's, I want to connect, I want to connect what we've promised with kind of like, what are the, what are the ideal, what is it?

[01:01:59] **Matthew Kerns**: not necessarily.

[01:01:59] **Matthew Kerns**: Yeah.

[01:02:00] **Matthew Kerns**: I'm necessarily ideal, but what is like 80% effectiveness, right?

[01:02:04] **Matthew Kerns**: Like the target for delivering on the experience.

[01:02:10] **Matthew Kerns**: And then we need to have, I want to have like in a document somewhere, like, okay, this, we have like a list of things that we think would be, would be great for this.

[01:02:30] **Matthew Kerns**: The integration.

[01:02:30] **Matthew Kerns**: then at certain point in time, when we think it's ready, we go one by one through that list.

[01:02:37] **Matthew Kerns**: And we verify that we have like one or more test cases of, okay, for this requirement, like a voicemail comes in.

[01:02:48] **Matthew Kerns**: Like, I don't even know if voicemail is actually a requirement as much anymore.

[01:02:51] **Matthew Kerns**: So maybe that's not a good example, but like a call comes in from a new client and

[01:03:00] **Matthew Kerns**: They have, like, they have, well, maybe existing clients better.

[01:03:06] **Matthew Kerns**: So a call comes in from an existing jobber client, and then we end up, we update, we create a request, and it has that jobber client.

[01:03:17] **Matthew Kerns**: Like, okay, boom, that test case is satisfied.

[01:03:21] **Matthew Kerns**: So I want, like, a long list of those and have some sort of measurable, like, okay, we're at, we're at 60 percent, we're at 70 percent, we're at 80 percent, and then as soon as you hit a certain number, then, cool.

[01:03:39] **Matthew Kerns**: Okay.

[01:03:39] **Chris Andrade**: Can can I, can I say something here, um, how, Matthew, how comfortable, like, you guys, both of y'all, if we roll this out tomorrow morning on a slow day, just to see what happens.

[01:03:54] **Chris Andrade**: Well, tomorrow, tomorrow is Saturday, right?

[01:03:56] **Trent Christopher**: Right.

[01:03:57] **Trent Christopher**: I mean, but just to test it.

[01:03:59] **Chris Andrade**: Saturday?

[01:04:00] **Chris Andrade**: No, but I'm just saying we can test it on a day that's where he's not off, to see how things just work, just turn it on like you're saying, and say, hey, we kind of just think we're at a point where we kind of want to test it, and since it's a weekend, do you mind?

[01:04:17] **Trent Christopher**: Yep, and Matthew is wanting to do his due diligence to make sure that we're meeting, we're meeting what we planned, what we achieved, that we can make sure that they merge and blend together, the plan and the merge.

[01:04:28] **Trent Christopher**: That they, you know, whenever we completed, what I would like to try to find a compromise here is that we don't have that list, I don't think right now, or, I don't, we're, we're three weeks in, since the fifth, right?

[01:04:48] **Trent Christopher**: Mm hmm.

[01:04:49] **Trent Christopher**: So, if look at the calendar, one, one, two, it's the end of the third week.

[01:04:58] **Chris Andrade**: Yeah.

[01:04:58] **Trent Christopher**: And I don't feel like we.

[01:05:00] **Trent Christopher**: We delivered on our promise, like we were going to do it in two weeks, but- Well, did we promise two weeks?

[01:05:06] **Trent Christopher**: No, we promised four, but- Right.

[01:05:10] **Trent Christopher**: We tried to set our own goal within two weeks, right?

[01:05:14] **Chris Andrade**: Right.

[01:05:14] **Trent Christopher**: But we also did say we were going to try to deploy it in week two, and then we were going to do evaluations in week three, and final release or whatever, handover with training and SOP or whatever.

[01:05:30] **Trent Christopher**: On week four.

[01:05:33] **Trent Christopher**: So, I want to make sure it's a solid solution for them.

[01:05:38] **Trent Christopher**: But at the same time, I don't want to push it for another week because we don't have a checklist completed.

[01:05:43] **Chris Andrade**: So that's why I asked if we can use this opportunity to kind of do a little benchmark test.

[01:05:49] **Chris Andrade**: Yeah, I think it's- I think it's a great idea because it's a weekend.

[01:05:54] **Matthew Kerns**: So they're, you know, if Alyssa doesn't- anyways.

[01:05:59] **Matthew Kerns**: find

[01:06:00] **Matthew Kerns**: She doesn't do on the weekend, right?

[01:06:02] **Matthew Kerns**: Like, she doesn't do stuff on the weekend?

[01:06:04] **Matthew Kerns**: Do any of them?

[01:06:06] **Matthew Kerns**: I don't know.

[01:06:07] **Chris Andrade**: know Kelsey does.

[01:06:08] **Chris Andrade**: He always takes phone calls.

[01:06:10] **Chris Andrade**: But I'm just saying, we could even just run test scenarios and test phone calls and just say, hey, I am Joe at, you know, testing university.

[01:06:19] **Chris Andrade**: We're just trying to test this system.

[01:06:22] **Chris Andrade**: I need a TX-50 and, you know, just run the test.

[01:06:26] **Trent Christopher**: Actually, we can flip it on and just say, Kelsey, test it.

[01:06:30] **Trent Christopher**: Let me get in a call real quick.

[01:06:32] **Chris Andrade**: Yeah.

[01:06:33] **Matthew Kerns**: So since he's our first.

[01:06:34] **Matthew Kerns**: Hold on.

[01:06:35] **Chris Andrade**: Hold on.

[01:06:36] **Chris Andrade**: Don't call him.

[01:06:36] **Chris Andrade**: Hold on.

[01:06:37] **Chris Andrade**: I'm not.

[01:06:38] **Chris Andrade**: Okay.

[01:06:38] **Chris Andrade**: I'm not.

[01:06:39] **Chris Andrade**: Okay.

[01:06:39] **Chris Andrade**: Matthew, go ahead.

[01:06:41] **Matthew Kerns**: I was going to say, like, since he's our friend and it's like, you know, we have this leeway, then I'm more okay with it.

[01:06:55] **Matthew Kerns**: But so like, it's kind of like my.

[01:07:00] **Matthew Kerns**: Like I should be making sure we have this type of thing.

[01:07:04] **Matthew Kerns**: I mean, and Trent's doing a great job because he's testing on his own account.

[01:07:08] **Matthew Kerns**: It's basically like staging environment.

[01:07:10] **Matthew Kerns**: Right.

[01:07:12] **Chris Andrade**: just trying to teach you guys like I think we want to draw some light to your work.

[01:07:17] **Matthew Kerns**: My point is, I think it's a great staging environment to use what they have on the weekend to deploy it live.

[01:07:28] **Matthew Kerns**: And then they can like we can literally see it working on their account and we can test scenarios and we can try and blow it up.

[01:07:39] **Matthew Kerns**: We can try and mess it up, you know, assuming we have time to work on it and then test out the bad scenarios that we think could be risky.

[01:07:49] **Matthew Kerns**: And then so we have permissions to go and edit stuff so we can we can do that.

[01:07:54] **Matthew Kerns**: And then like next week, while it's running, assuming we don't have to roll.

[01:08:01] **Matthew Kerns**: And then we can build out the checklist and do our diligence kind of like in parallel I think it would be a really cool thing and then I know he's gonna nerd out with it and him and his wife are gonna mess around and say go crazy guys break it.

[01:08:17] **Chris Andrade**: Let's use this weekend and this like have fun and then and then let's see what happens.

[01:08:22] **Chris Andrade**: Yeah, yeah, that'd be cool to help to So you just let me know when you want me to make the phone call.

[01:08:34] **Trent Christopher**: Um, I'm, I mean, Matthew you want to you want to do any more due diligence here before we get the real.

[01:08:42] **Matthew Kerns**: I, I mean, it would be cool to have like a few hours where I can go in.

[01:08:50] **Matthew Kerns**: Like right now I have, I've got a workout and four hours I want to get there but I have like two or three hours where I can, I can do this I can go in and just.

[01:09:00] **Matthew Kerns**: Pull in the latest, try and get familiar and test out things, and then just note down stuff, and then I don't think I should necessarily block anything unless there's something crazy, but I doubt there will be.

[01:09:18] **Matthew Kerns**: But, yeah, I mean, I think like, what are we thinking like tomorrow, tomorrow morning, we go live, we should at least have our rollback procedure, like, like figured out so that just in case, like, okay, worst, if you think worst case scenario.

[01:09:40] **Matthew Kerns**: Is it at all possible that their jobber information gets compromised?

[01:09:48] **Trent Christopher**: That would be my biggest concern, is that, and actually, the only thing that I feel is a bit of a risk is the contacts.

[01:10:00] **Trent Christopher**: And the reason is because there's potential, since we are creating new contacts, that we could overlap somewhere, or we could put garbage in it.

[01:10:13] **Trent Christopher**: Is there a way to back it up prior, like versionize it?

[01:10:17] **Trent Christopher**: I think so.

[01:10:18] **Trent Christopher**: Let me see.

[01:10:19] **Trent Christopher**: So versionize it, document, like almost like iCloud, right?

[01:10:25] **Chris Andrade**: Yeah, let me see if I can back it up.

[01:10:28] **Chris Andrade**: What's that time lapse, time machine?

[01:10:31] **Matthew Kerns**: We have a problem with getting a snapshot of the current jobber, which is, if we're adding stuff with our integration, and then they get a real new contact, then if we roll back to that previous version, we need to go in and figure out who are the real contacts.

[01:10:49] **Trent Christopher**: Well, we can do that by comparing.

[01:10:50] **Trent Christopher**: What you do is you save the current version, then later you get the newest version.

[01:10:59] **Trent Christopher**: So you you

[01:11:00] **Trent Christopher**: Compare the two, and then you have to have a weed-out process where you're removing the garbage that we might have injected.

[01:11:06] **Matthew Kerns**: Yep.

[01:11:07] **Matthew Kerns**: And then we put the good version back in.

[01:11:10] **Trent Christopher**: Yeah.

[01:11:11] **Matthew Kerns**: And we'll have our logs.

[01:11:14] **Chris Andrade**: Do you guys, Trent, I would be curious to see what's your, like, do you, how do you keep track of versioning yourself and Matthew, both of'all?

[01:11:23] **Chris Andrade**: Right now, GitHub is the primary way to do versioning.

[01:11:29] **Trent Christopher**: Oh, I see.

[01:11:30] **Chris Andrade**: So they, like, automatically, like, populate a version?

[01:11:34] **Trent Christopher**: Well, that's actually the primary purpose of GitHub.

[01:11:39] **Trent Christopher**: Interesting.

[01:11:40] **Trent Christopher**: Yeah.

[01:11:41] **Chris Andrade**: Interesting.

[01:11:41] **Chris Andrade**: Yeah.

[01:11:42] **Chris Andrade**: you.

[01:11:42] **Chris Andrade**: Yeah.

[01:11:43] **Chris Andrade**: Yep.

[01:11:44] **Trent Christopher**: That's the primary purpose of is all revision control.

[01:11:47] **Trent Christopher**: Interesting.

[01:11:48] **Trent Christopher**: you can make revisions and you can keep track of it and branch it and copy it and all kinds of crazy.

[01:11:56] **Trent Christopher**: I don't know how it incorporated in a construction.

[01:12:00] **Chris Andrade**: Yeah.

[01:12:02] **Trent Christopher**: So I'm trying to see if I can find where I can export the data.

[01:12:07] **Trent Christopher**: So anyway, what do you think, Matthew?

[01:12:10] **Trent Christopher**: We export it, and then we just give it a shot.

[01:12:15] **Trent Christopher**: Anyway, I'll just come back.

[01:12:17] **Trent Christopher**: I got a little derailed.

[01:12:18] **Trent Christopher**: So I'm not worried about the requests, because the requests are something they weren't really using before.

[01:12:25] **Trent Christopher**: Yeah.

[01:12:26] **Trent Christopher**: And it doesn't affect jobs and quotes and all that stuff that they have existing in their system.

[01:12:34] **Trent Christopher**: It's an additional feature.

[01:12:36] **Trent Christopher**: We're not even touching jobs and quotes and all those things.

[01:12:40] **Trent Christopher**: We're just doing the request and adding notes to the request.

[01:12:44] **Trent Christopher**: Yep.

[01:12:45] **Trent Christopher**: So that's kind of in its own little island.

[01:12:47] **Trent Christopher**: But the contacts is affected across the whole system.

[01:12:51] **Matthew Kerns**: So the question about the contacts where we can create new contacts, or do we have any functionality that

[01:13:02] **Matthew Kerns**: I don't think it's updating it.

[01:13:04] **Trent Christopher**: I think what we're doing is we are literally just saying, if it exists, just use what's in Jobber and leave the rest of it alone.

[01:13:12] **Trent Christopher**: Okay.

[01:13:13] **Matthew Kerns**: Let me just verify that real quick.

[01:13:15] **Trent Christopher**: But I think I'm pretty sure that is what we ended up with.

[01:13:20] **Trent Christopher**: Because we did go through a point where I thought maybe it'd be good idea to try to update contacts, but then I got concerned about butchering them on accident.

[01:13:34] **Trent Christopher**: Yeah, exactly.

[01:13:36] **Trent Christopher**: So at that point, I was like, you know what, it might be best to just prioritize Jobber contacts, at least for now.

[01:13:43] **Trent Christopher**: And if for any reason they need to update it, they have to update it manually.

[01:13:47] **Trent Christopher**: Like it's not being updated through our system right now.

[01:13:51] **Trent Christopher**: That sounds good.

[01:13:52] **Matthew Kerns**: Yeah.

[01:13:52] **Matthew Kerns**: It's the safe way to do it.

[01:13:54] **Trent Christopher**: But maybe in the future, once we build more confidence in the system, we can consider it.

[01:14:00] **Chris Andrade**: All right.

[01:14:03] **Trent Christopher**: Anyway, so any other thoughts there, Matthew?

[01:14:07] **Trent Christopher**: And then if you want to, we can call Kelsey real quick.

[01:14:09] **Trent Christopher**: I don't I'm going to give you a heads up.

[01:14:10] **Trent Christopher**: I don't want to be on here until seven.

[01:14:12] **Trent Christopher**: So it's it's 610 here now.

[01:14:15] **Chris Andrade**: So well, I mean, if you want to develop a plan, and then I can call him tomorrow morning, because I'm going to see him at church tomorrow.

[01:14:22] **Chris Andrade**: I can just do that.

[01:14:23] **Chris Andrade**: I don't have time to mess with it tomorrow.

[01:14:26] **Trent Christopher**: Okay, that's fine.

[01:14:29] **Chris Andrade**: So roll it out like right now.

[01:14:32] **Trent Christopher**: Yeah, if we're going to do it, would probably just try to roll it out like now.

[01:14:36] **Chris Andrade**: Are you already have the backup initiated or something?

[01:14:40] **Trent Christopher**: I'm, I'm trying to find out if I can export the context so that we don't if for any reason, something goes haywire, we don't want to worry about it.

[01:14:47] **Trent Christopher**: Now, I don't want you to be telling him that we're concerned about right?

[01:14:53] **Trent Christopher**: No, no.

[01:14:54] **Trent Christopher**: Right, right.

[01:14:54] **Chris Andrade**: Yeah.

[01:14:55] **Chris Andrade**: But you can tell him we're going to back it up.

[01:14:57] **Chris Andrade**: I that we have a copy.

[01:14:58] **Chris Andrade**: I can get of can get out it.

[01:15:00] **Chris Andrade**: I just like to have all the bases covered, I guess, you know?

[01:15:05] **Chris Andrade**: I don't want to incite panic because we're considering all the cases here.

[01:15:13] **Chris Andrade**: So what do you want to do?

[01:15:16] **Chris Andrade**: You're looking at how to back this up, correct?

[01:15:18] **Chris Andrade**: On Jobber?

[01:15:20] **Chris Andrade**: Yeah, I'm doing a couple different things.

[01:15:22] **Chris Andrade**: While we can do that, do you mind me going through some stuff?

[01:15:26] **Chris Andrade**: Or, like, just talking?

[01:15:29] **Matthew Kerns**: How do we actually, maybe, Chris, maybe me and you can sync up later, because we gotta, if Trent can only be on here for another 45 minutes, we gotta prioritize.

[01:15:38] **Chris Andrade**: I just, I just, well, all I'm trying to just make an emphasis to Trent is like, I just want him to know how much I value your effort, and your talent.

[01:15:51] **Chris Andrade**: Dude, like, what I'm, I just preach, like, what you're showing me, like, completely, I understand, like, your maker time, damn, dog.

[01:15:59] **Chris Andrade**: You and

[01:16:00] **Chris Andrade**: Nathan, like, hell yeah, like, this is some good stuff, and yeah, I want to second that also, because there's been a lot of progress this week, and it's all pretty much awesome, so it's cool.

[01:16:12] **Chris Andrade**: And I totally get it, because I'm learning how to speak y'all's language, and try to read the lines, because we all have our way of communicating, right, and I try to anticipate you guys at the end of the day more than anybody else, because if I can figure out how to hand you that piece of paper before you ask for it, I feel like I'm doing my job, you know, and all I would just want to just mention to you is like, this is, you're making us so much better, and I just, that work with your health awareness is like, it's not going to change our lives, but like my parents life, my mom's life, like Kelsey's life, all of that is going to be...

[01:16:59] **Chris Andrade**: all be...

[01:17:01] **Chris Andrade**: And gives a baseline, a north star, beacon of where just to get an answer And I just want to let you know that it is valued beyond recognition, my friend So I just wanted to make sure you're aware of that Appreciate it.

[01:17:17] **Trent Christopher**: And thanks for everything you do, too.

[01:17:19] **Trent Christopher**: Thanks, Chris This is so much fun, man.

[01:17:25] **Trent Christopher**: This is so much fun Okay, so Contact Handling Summary Workflow uses ClientEdit to update existing contacts when an exact phone number or match is found in any of these conditions.

[01:17:40] **Trent Christopher**: New emails to add.

[01:17:41] **Trent Christopher**: It does add new emails and it does add phone numbers Sorry, are you looking at, like, I don't know if I can see what you're saying on your screen.

[01:17:49] **Trent Christopher**: Yeah, you can't hear So I just I just was asking it over here on the right

[01:18:00] **Trent Christopher**: It said, contacts are updated, not just created.

[01:18:06] **Trent Christopher**: Updates are limited in scope.

[01:18:08] **Trent Christopher**: So let's look at that real quick.

[01:18:09] **Trent Christopher**: The update logic is in this flow here.

[01:18:13] **Trent Christopher**: It uses client edit GraphQL mutation to update existing clients when an exact phone match is found.

[01:18:19] **Trent Christopher**: So first of all, it has to match an exact phone number and any of these conditions exist.

[01:18:25] **Trent Christopher**: A new email to add that's not already on the client.

[01:18:29] **Trent Christopher**: A new phone number to add.

[01:18:32] **Trent Christopher**: Client has a placeholder name.

[01:18:36] **Trent Christopher**: And, this is an and.

[01:18:39] **Matthew Kerns**: It's an and any though.

[01:18:41] **Matthew Kerns**: So quick question about exact phone match.

[01:18:44] **Matthew Kerns**: That's, is that for sure Jobber phone match?

[01:18:50] **Matthew Kerns**: Jobber.

[01:18:51] **Matthew Kerns**: Yeah.

[01:18:51] **Trent Christopher**: Jobber has an, uh, an API that you can search by phone number.

[01:18:57] **Trent Christopher**: Okay.

[01:18:58] **Matthew Kerns**: So it's, it's finding the.

[01:19:00] **Trent Christopher**: The number of the client in jobber, and it's searching by the phone number.

[01:19:08] **Trent Christopher**: Okay.

[01:19:10] **Trent Christopher**: Because the jobber client.

[01:19:19] **Trent Christopher**: Gosh, why am I even typing?

[01:19:24] **Chris Andrade**: By the way, update.

[01:19:26] **Chris Andrade**: S&S Woolsheds, me and my brother had an amazing meeting.

[01:19:30] **Chris Andrade**: Bro, I sold the ticket.

[01:19:32] **Chris Andrade**: I know how this is going to roll out.

[01:19:35] **Chris Andrade**: So we'll have a signed contract with S&S by January.

[01:19:38] **Chris Andrade**: I bet February 1.

[01:19:40] **Chris Andrade**: Nice.

[01:19:40] **Trent Christopher**: Nice.

[01:19:41] **Trent Christopher**: That's good.

[01:19:43] **Trent Christopher**: So it'll add phone numbers, it will add emails, and it will only modify the current name of the placeholder.

[01:19:50] **Trent Christopher**: So only if it's something like quo lead.

[01:19:54] **Trent Christopher**: Okay.

[01:19:58] **Trent Christopher**: It doesn't update existing.

[01:20:13] **Trent Christopher**: Okay, so let me ask this real quick.

[01:20:15] **Trent Christopher**: So I just asked that client search is using the phone number.

[01:20:19] **Trent Christopher**: So here's the search terms.

[01:20:20] **Trent Christopher**: So it says find the number by phone right here.

[01:20:26] **Trent Christopher**: So search client by phone.

[01:20:30] **Trent Christopher**: Search phone.

[01:20:32] **Trent Christopher**: Find the first five.

[01:20:33] **Trent Christopher**: It searches for the first five.

[01:20:37] **Trent Christopher**: Passes the cell phone number.

[01:20:39] **Trent Christopher**: It returns five potential matches.

[01:20:44] **Trent Christopher**: It normalizes and then compares it to make sure they're in the same format.

[01:20:50] **Trent Christopher**: Two-step.

[01:20:51] **Trent Christopher**: Fuzzy search for phone using a job or search term.

[01:20:56] **Trent Christopher**: Exact verification by normalizing and comparing ten digit phone numbers.

[01:21:00] **Trent Christopher**: No email or name matching is used for the primary lookup, only phone.

[01:21:05] **Matthew Kerns**: Okay, so if there's a number that gets called that matches a Jobber, it's basically the only time that we update a Jobber client.

[01:21:17] **Matthew Kerns**: Correct.

[01:21:18] **Matthew Kerns**: Which makes sense.

[01:21:19] **Matthew Kerns**: It has to match in Jobber.

[01:21:22] **Trent Christopher**: If it does not match explicitly the phone number in Jobber, it doesn't do anything with it.

[01:21:26] **Trent Christopher**: Well, it doesn't update the existing client, it'll create a new one.

[01:21:33] **Trent Christopher**: If for any reason they need to merge that particular contact with an existing client, it has to be manual.

[01:21:41] **Trent Christopher**: At this point in time.

[01:21:44] **Trent Christopher**: There's no mechanism in Jobber's UI to do that.

[01:21:49] **Trent Christopher**: So we would have to build that function and that's not in scope.

[01:21:55] **Trent Christopher**: Yeah.

[01:21:58] **Trent Christopher**: Because it would require a

[01:22:00] **Trent Christopher**: Like an interface for Alyssa or something.

[01:22:02] **Trent Christopher**: Like we'd have to create something where Alyssa would have to say, merge this contact with this contact.

[01:22:09] **Trent Christopher**: And we'd have to give her a UI for that.

[01:22:13] **Matthew Kerns**: Yeah, I mean, there's a way to do additional contacts for a client.

[01:22:19] **Matthew Kerns**: So we could consider doing that too.

[01:22:23] **Trent Christopher**: We could potentially, this is just potentially, we could potentially use Claude mobile or Claude desktop to connect to something and potentially ask it to do that.

[01:22:32] **Trent Christopher**: But we should do some very thorough testing before we do that.

[01:22:36] **Trent Christopher**: Yeah.

[01:22:38] **Chris Andrade**: Yeah.

[01:22:38] **Matthew Kerns**: And I'll just allow it to go in.

[01:22:41] **Matthew Kerns**: Yeah.

[01:22:41] **Trent Christopher**: I mean, we would probably put, we would put deterministic logic in N8N and use it as a tool like an MCP server so that Claude has access to it.

[01:22:54] **Trent Christopher**: But we have control over validity.

[01:22:56] **Trent Christopher**: Yeah.

[01:22:57] **Trent Christopher**: Yeah.

[01:22:58] **Chris Andrade**: Yeah.

[01:22:58] **Chris Andrade**: Thank you.

[01:22:59] **Matthew Kerns**: Yeah.

[01:23:00] **Matthew Kerns**: Okay.

[01:23:01] **Matthew Kerns**: How, I have question.

[01:23:02] **Matthew Kerns**: How do you, how do we connect this?

[01:23:04] **Matthew Kerns**: How do we launch it?

[01:23:06] **Chris Andrade**: How do we connect it and switch it?

[01:23:08] **Trent Christopher**: Yeah.

[01:23:09] **Trent Christopher**: I have to disconnect it from mine and then connect it to their jobber.

[01:23:15] **Trent Christopher**: So it's actually pretty easy.

[01:23:17] **Trent Christopher**: All you do is log in under the correct jobber account and then, um, so like I could, I could, cause I want to make sure that I could roll it back too.

[01:23:36] **Matthew Kerns**: Um, so is there a way that, cause I have access, my account has access to their jobber, right?

[01:23:41] **Matthew Kerns**: is there a way that I could disconnect it?

[01:23:45] **Trent Christopher**: I think the best way or the, the intended way to disconnect it is literally go into jobber and click disconnect.

[01:23:55] **Trent Christopher**: Okay.

[01:23:55] **Trent Christopher**: So disconnect button in your jobber.

[01:23:58] **Matthew Kerns**: Connected apps here.

[01:24:00] **Matthew Kerns**: Okay.

[01:24:00] **Matthew Kerns**: If you just go to apps.

[01:24:02] **Trent Christopher**: And then to restore their function.

[01:24:06] **Trent Christopher**: not even apps.

[01:24:07] **Trent Christopher**: You would actually go to settings.

[01:24:13] **Trent Christopher**: So you go to settings in here and right here where says arise testing.

[01:24:17] **Trent Christopher**: go to arise testing and hit disconnect.

[01:24:20] **Matthew Kerns**: And then for our arise testing to work, do we need to disconnect their Quo connection?

[01:24:29] **Matthew Kerns**: No.

[01:24:30] **Trent Christopher**: I'm, I'm currently connected to Quo.

[01:24:32] **Trent Christopher**: Wait, wait, hold on.

[01:24:33] **Trent Christopher**: Which, which connection are you talking about?

[01:24:35] **Trent Christopher**: Are you talking about like quota job or integration?

[01:24:39] **Trent Christopher**: The existing, uh, the existing inherent integration?

[01:24:44] **Trent Christopher**: Yes.

[01:24:45] **Matthew Kerns**: Yes.

[01:24:45] **Matthew Kerns**: We need to disconnect that.

[01:24:46] **Trent Christopher**: We don't want to do both.

[01:24:47] **Trent Christopher**: Cause if we do both, we're going to get, they're going to get double.

[01:24:50] **Trent Christopher**: Yeah.

[01:24:52] **Trent Christopher**: Okay.

[01:24:52] **Matthew Kerns**: So then the re the disconnect process, we would want to have them.

[01:25:00] **Matthew Kerns**: They would, or wait, we could connect Quo to Jobber, right?

[01:25:05] **Matthew Kerns**: Because we have access to their Quo.

[01:25:06] **Trent Christopher**: We have access to Quo and Jobber and this N8N, but you know, the only place that needs to be switched is in Jobber.

[01:25:17] **Trent Christopher**: Nothing else needs to change.

[01:25:19] **Trent Christopher**: Like right now, it's fully functional.

[01:25:21] **Trent Christopher**: It's just working with my Jobber.

[01:25:24] **Trent Christopher**: So really all we need to do is just switch it from my Jobber to their Jobber.

[01:25:27] **Trent Christopher**: Yeah.

[01:25:28] **Matthew Kerns**: I just want to make sure I have the rollback procedure just in case, because I know that you said it'd be out in the morning.

[01:25:34] **Matthew Kerns**: Yeah.

[01:25:35] **Trent Christopher**: Here's what the rollback process is.

[01:25:36] **Trent Christopher**: Okay.

[01:25:37] **Trent Christopher**: I'll take my laptop with me, but I'm going to my niece's birthday party, so I can still help.

[01:25:43] **Trent Christopher**: I just won't be active, if that makes sense.

[01:25:47] **Chris Andrade**: So this is my plan.

[01:25:48] **Chris Andrade**: This is my plan.

[01:25:49] **Chris Andrade**: Since I'm going to church with him tomorrow morning, I presume church will be over around 730, right?

[01:25:55] **Chris Andrade**: right.

[01:25:56] **Chris Andrade**: I'm saying, hey Kelsey, by the way.

[01:26:00] **Chris Andrade**: What if we can turn on a feature to show you, like, we need to test something?

[01:26:06] **Chris Andrade**: Would you be like, can we test it on the weekend?

[01:26:08] **Chris Andrade**: He's aware.

[01:26:09] **Chris Andrade**: I mean, he's aware of what I've been doing.

[01:26:11] **Chris Andrade**: Okay, so can we turn it on?

[01:26:14] **Trent Christopher**: He's been asking me, or he's been referring to my work as Trent's plugin.

[01:26:21] **Trent Christopher**: So if you want to, you could say, hey, is it okay if we go ahead and swap over with Trent's plugin and you can start testing it over the weekend with whatever random stuff you want to do?

[01:26:28] **Chris Andrade**: So after the church ceremony, I could come up to him and like, I could go like, can you record it?

[01:26:33] **Chris Andrade**: I'll record it.

[01:26:34] **Chris Andrade**: Yeah, that's what I'll do.

[01:26:35] **Chris Andrade**: I'll record it.

[01:26:37] **Chris Andrade**: Because I want to capture that  and be like, hey, can we turn on Trent's plugin and like test it over the weekend?

[01:26:44] **Chris Andrade**: So are we thinking to turn it tomorrow?

[01:26:46] **Matthew Kerns**: I we were thinking to turn it on right now.

[01:26:47] **Matthew Kerns**: I mean, I would turn it on right now.

[01:26:50] **Chris Andrade**: I'm just saying for the gravitas, right?

[01:26:55] **Chris Andrade**: Because he's going to be all fired up after church.

[01:26:58] **Chris Andrade**: I know it.

[01:26:59] **Chris Andrade**: And then they'll be like.

[01:27:06] **Trent Christopher**: So here's the process to disconnect it.

[01:27:12] **Trent Christopher**: The rollback plan is literally right now.

[01:27:16] **Chris Andrade**: you want it, I'm just saying whatever you want.

[01:27:21] **Trent Christopher**: What do you want to do, Matthew?

[01:27:22] **Trent Christopher**: I don't really care.

[01:27:23] **Trent Christopher**: I mean, I just, I just want to make sure I'm off here before seven.

[01:27:32] **Matthew Kerns**: Yeah, I mean, it might be.

[01:27:36] **Matthew Kerns**: Why don't we go through the rollback?

[01:27:38] **Matthew Kerns**: And then as soon as as long as I know that I can do that, or like, I mean, you'll have access to as long as we know what that process is, then we can roll it back.

[01:27:47] **Matthew Kerns**: So there's no reason to not turn it on.

[01:27:49] **Matthew Kerns**: Okay, here's step by step.

[01:27:52] **Trent Christopher**: Step by step, Ali, you roll it back.

[01:27:54] **Trent Christopher**: Let's, we're going to assume, we're going to assume that we are connected to their jobber.

[01:27:59] **Trent Christopher**: see later.

[01:28:00] **Trent Christopher**: And I'm looking at their jobber right here.

[01:28:02] **Trent Christopher**: This is an assumption, okay?

[01:28:04] **Trent Christopher**: So you're going to click, you're going to go to Settings.

[01:28:07] **Trent Christopher**: You're going to go to Settings.

[01:28:09] **Trent Christopher**: You're going go down here where it says Arise Testing, because that's what my app is called, Arise Testing.

[01:28:13] **Trent Christopher**: So then we're going to click Disconnect.

[01:28:18] **Trent Christopher**: Okay?

[01:28:19] **Trent Christopher**: So now it's disconnected.

[01:28:22] **Trent Christopher**: The next thing you need to do is you need to go to Apps.

[01:28:27] **Trent Christopher**: You need to go to Quo.

[01:28:29] **Trent Christopher**: But you need to be logged in under Quo, I think.

[01:28:32] **Trent Christopher**: So you would go to Quo, and you would hit Connect.

[01:28:37] **Trent Christopher**: And if you're not logged in, you need to make sure you're logged in under Quo.

[01:28:42] **Matthew Kerns**: And how do we make sure that Quo to Java connection works?

[01:28:46] **Matthew Kerns**: What Quo account do I need to be logged into?

[01:28:51] **Trent Christopher**: There's.

[01:28:52] **Trent Christopher**: Which one?

[01:28:53] **Matthew Kerns**: Like, do I have the credentials for that?

[01:28:54] **Trent Christopher**: This is using OAuth 2 with your local browser.

[01:28:59] **Trent Christopher**: So...

[01:29:00] **Trent Christopher**: So it's whatever you're logged into.

[01:29:02] **Trent Christopher**: So if you log in under Quo, okay, I can give you login information.

[01:29:07] **Trent Christopher**: Yes, that's what I need.

[01:29:08] **Matthew Kerns**: Okay.

[01:29:09] **Trent Christopher**: Well, I can give it to you.

[01:29:10] **Trent Christopher**: I can say it here, but I don't know if that's best practice.

[01:29:15] **Matthew Kerns**: Yeah, maybe give it to me offline, I guess.

[01:29:18] **Matthew Kerns**: Yeah, I can give it to you offline, no problem.

[01:29:19] **Trent Christopher**: So make sure that I give that to you.

[01:29:24] **Trent Christopher**: Okay, but you need to go in and you need to log in.

[01:29:25] **Trent Christopher**: So once you're logged in, which I will just go in and do it right now, you won't be able to see the password because it'll be dotted out.

[01:29:33] **Trent Christopher**: So you have to be logged in under Quo.

[01:29:44] **Trent Christopher**: So as long as you're under Kelsey logged in, okay, then you can go here and you can hit allow access and it'll connect it.

[01:29:53] **Trent Christopher**: Yep.

[01:29:54] **Trent Christopher**: It uses whatever you're currently logged in as in your local browser here.

[01:30:01] **Matthew Kerns**: I thought he shaved his beard.

[01:30:05] **Trent Christopher**: He did, shaved it, but this is the old.

[01:30:08] **Trent Christopher**: Yeah, I like it.

[01:30:09] **Trent Christopher**: So that's really all you would do there.

[01:30:12] **Trent Christopher**: Now, the trickiest part is that I would have to give you a login for this.

[01:30:18] **Trent Christopher**: So, like I just showed you, if you need to re-establish the connection from N8N, to do that, you would go to, you don't do anything in here, but you have to be logged into the correct, whatever the correct Jobber account you want.

[01:30:34] **Trent Christopher**: Because this is, again, this is OAuth 2.

[01:30:37] **Trent Christopher**: So, it's whatever account you're logged into.

[01:30:39] **Trent Christopher**: You go into N8N, which I'll have to give you the login to my, this is my instance.

[01:30:46] **Trent Christopher**: And then go to Credentials, Jobber, and then Reconnect.

[01:30:56] **Matthew Kerns**: See, so this, we then...

[01:31:00] **Matthew Kerns**: Once it's running, we have a problem of where are you going to work on stuff.

[01:31:06] **Matthew Kerns**: So we kind of want to have like a production endpoint for a server endpoint.

[01:31:12] **Matthew Kerns**: Correct.

[01:31:13] **Matthew Kerns**: This will be for testing.

[01:31:15] **Trent Christopher**: We're going to have to migrate this to a production instance.

[01:31:20] **Trent Christopher**: Yep.

[01:31:21] **Trent Christopher**: Correct.

[01:31:21] **Chris Andrade**: This will be for testing.

[01:31:23] **Trent Christopher**: We'll be able to turn it on.

[01:31:25] **Trent Christopher**: We'll be able to test it.

[01:31:26] **Trent Christopher**: And then if for any reason, we can switch it off.

[01:31:30] **Trent Christopher**: But then we need to migrate it to production once we think that we're ready for that.

[01:31:36] **Trent Christopher**: Whatever the criteria we decide for that.

[01:31:39] **Matthew Kerns**: Yeah, that sounds good.

[01:31:44] **Matthew Kerns**: And then, yeah, and then in the future, I think even for testing, we want to have a separate environment so that when issues come up in testing, or if issues come up, we have a separate environment where we can work because we might not.

[01:31:59] **Matthew Kerns**: You mean.

[01:31:59] **Matthew Kerns**: mean.

[01:32:00] **Trent Christopher**: Production and testing, like running in parallel?

[01:32:04] **Matthew Kerns**: Yeah, like staging, like, well, production, and then we, at least we need to have production, and then we need to have something each of us can test, like you have your own testing environment, I have my own testing environment.

[01:32:18] **Matthew Kerns**: Well, that's what these are for.

[01:32:21] **Trent Christopher**: Yeah, or maybe they're not, maybe these are just our sandbox for us to play around in.

[01:32:24] **Trent Christopher**: And then we have a separate one that's specific just for dev, a dev server, right?

[01:32:31] **Trent Christopher**: So, I mean, it can be plotter mechanics dev if we wanted to, or PM for plotter mechanics dev, but whatever, we can make our own dev instance, but then we need to have a production instance that is not being touched while we're doing testing and development, right?

[01:32:51] **Matthew Kerns**: Yeah, I think that's the most important one, the production one, so let's, maybe we'll just focus on doing that one.

[01:32:58] **Matthew Kerns**: mean, uh,

[01:33:00] **Matthew Kerns**: And then as long as we have a separate environment to test in, like it's our sandbox for now, think that's okay for now.

[01:33:07] **Matthew Kerns**: Yeah, and we do.

[01:33:08] **Trent Christopher**: We have these, the TCN8N and you have your MK.

[01:33:11] **Trent Christopher**: Yeah.

[01:33:12] **Trent Christopher**: So, all right, so.

[01:33:15] **Matthew Kerns**: We can use Chris's as the production one, assuming he won't push anything, but.

[01:33:20] **Trent Christopher**: I have a production one, but I really meant it to be for our use cases for Arise production.

[01:33:28] **Trent Christopher**: Okay, but we're not using it right now.

[01:33:31] **Matthew Kerns**: How tough is it to set up a new URL?

[01:33:34] **Matthew Kerns**: Just real quick.

[01:33:36] **Trent Christopher**: I mean, it's not super hard to set up a new URL.

[01:33:41] **Trent Christopher**: The thing is, is I'm trying to figure out where we're going to host it because technically by the license terms, we can't host it.

[01:33:49] **Trent Christopher**: We're violating the license by hosting it.

[01:33:52] **Trent Christopher**: Why is that?

[01:33:54] **Chris Andrade**: It has to be on his infrastructure.

[01:33:57] **Trent Christopher**: So, he has to have a server in his shop?

[01:33:59] **Chris Andrade**: Thank

[01:34:00] **Chris Andrade**: He has to own the infrastructure.

[01:34:02] **Trent Christopher**: That just means his name has to be on him.

[01:34:04] **Trent Christopher**: He doesn't have to server, but it can't be ours.

[01:34:08] **Trent Christopher**: It needs to be, we can run it in Railway on the- What is it?

[01:34:16] **Chris Andrade**: N8n, what I'm showing right now, N8n.

[01:34:18] **Trent Christopher**: Okay, the instance, so, okay, got it.

[01:34:21] **Chris Andrade**: Okay, interesting.

[01:34:22] **Trent Christopher**: We can run it in the cloud somewhere, so that it can continue running, and we have easier access to manage it.

[01:34:30] **Trent Christopher**: But technically, we are not supposed to be hosting it as a production solution that we have charged money for.

[01:34:38] **Trent Christopher**: And really, actually, we're not even supposed to be hosting it.

[01:34:42] **Chris Andrade**: I guess I just need more clarity down the road on that, but we'll table that.

[01:34:48] **Chris Andrade**: What's that, like, what's that topic called?

[01:34:51] **Chris Andrade**: Who's just, what license are we in violation of?

[01:34:57] **Chris Andrade**: N8n licensing, right?

[01:34:59] **Chris Andrade**: Who's, who's, who's, who's,

[01:35:00] **Trent Christopher**: It's right now.

[01:35:01] **Trent Christopher**: It's when it goes to production and we're going to leave it.

[01:35:04] **Trent Christopher**: It can't be hosted on our servers.

[01:35:07] **Chris Andrade**: I guess at that point, then I'll just need clarification when we get there, but okay.

[01:35:11] **Chris Andrade**: So I think I vote Trent, if you guys want to roll this out, I think Trent or maybe Matthew, you guys, you guys earned the right to call Kelsey and give him the good news.

[01:35:22] **Chris Andrade**: And if that's what you guys want to do tonight.

[01:35:28] **Trent Christopher**: I don't care if we, I, to be honest, if I'm just flipping it over from one to the other, I can do it anytime.

[01:35:34] **Trent Christopher**: Well, as long as I'm not like in the middle of something.

[01:35:38] **Trent Christopher**: So, so I have a way to flip it back now.

[01:35:41] **Matthew Kerns**: So I think I'm assuming I get the recording, but I think I'm good to, if we want to just do that now, what do you guys think?

[01:35:53] **Chris Andrade**: Call him first and just make sure he's already going to do that first.

[01:35:57] **Chris Andrade**: Yeah, let's, let's just call him real quick.

[01:35:58] **Trent Christopher**: I just want to make sure I'm not going

[01:36:00] **Trent Christopher**: Be on your own mic.

[01:36:00] **Trent Christopher**: That's all.

[01:36:01] **Trent Christopher**: I know that, you know, Kelsey's gonna get all fired up and he's gonna want to talk about a bunch of stuff.

[01:36:05] **Trent Christopher**: So if we can just try to zero in on getting this turned on and he's okay with it.

[01:36:10] **Trent Christopher**: If you guys want to keep chatting, you can go ahead and do it and I can jump off or something.

[01:36:15] **Matthew Kerns**: Should we, do you want to get like one click away before we call him?

[01:36:19] **Matthew Kerns**: Or what do you think is the best way to do this?

[01:36:21] **Trent Christopher**: I mean, I'm mostly, I mean, all I really have to do, you can call him whenever it's fine.

[01:36:27] **Trent Christopher**: Okay.

[01:36:28] **Chris Andrade**: Are you gonna call Matthew?

[01:36:32] **Chris Andrade**: What?

[01:36:32] **Matthew Kerns**: Oh, uh, I was thinking you would call him, Yeah.

[01:36:40] **Trent Christopher**: So to, to, establish it, I'm just logging in under the correct account.

[01:36:45] **Chris Andrade**: Okay.

[01:36:48] **Matthew Kerns**: This is Chris.

[01:36:53] **Chris Andrade**: Hold on.

[01:36:54] **Chris Andrade**: Did you guys hear that?

[01:36:56] **Chris Andrade**: Nope.

[01:36:58] **Matthew Kerns**: Nope.

[01:37:00] **Chris Andrade**: My personal number, if this has to do with words.

[01:37:04] **Chris Andrade**: Oh.

[01:37:08] **Trent Christopher**: Interesting.

[01:37:10] **Trent Christopher**: Sorry, it's all wrong.

[01:37:14] **Chris Andrade**: Let text him.

[01:37:16] **Matthew Kerns**: All I heard was this is Kelsey's personal number.

[01:37:19] **Matthew Kerns**: He tried to set up something today while he was at the office.

[01:37:24] **Trent Christopher**: What phone number did you ring?

[01:37:27] **Trent Christopher**: This is just personal.

[01:37:29] **Chris Andrade**: The 480-416-9780.

[01:37:35] **Chris Andrade**: Okay, yeah, that's his new one.

[01:37:37] **Trent Christopher**: So, oh, what's the number that you put in?

[01:37:46] **Trent Christopher**: Let me try calling his other number.

[01:37:52] **Trent Christopher**: Let me just try calling that one.

[01:37:53] **Trent Christopher**: This one should ring in.

[01:37:58] **Trent Christopher**: It's going to be.

[01:37:59] **Trent Christopher**: Thank

[01:38:13] **Chris Andrade**: My printer is broken.

[01:38:14] **Chris Andrade**: I need help.

[01:38:15] **Chris Andrade**: My printer broke.

[01:38:18] **Chris Andrade**: No, no, no.

[01:38:19] **Chris Andrade**: It's Chris.

[01:38:20] **Chris Andrade**: It's Chris.

[01:38:20] **Chris Andrade**: It's Chris.

[01:38:20] **Chris Andrade**: I'm joking.

[01:38:21] **Chris Andrade**: joking.

[01:38:21] **Chris Andrade**: Chris.

[01:38:24] **Chris Andrade**: Oh, I'm sorry.

[01:38:29] **Chris Andrade**: I got Trent and Matthew on the line.

[01:38:33] **Chris Andrade**: We did a stress test.

[01:38:34] **Chris Andrade**: We wanted to see if you were...

[01:38:39] **Chris Andrade**: Okay, so I got Matthew.

[01:38:41] **Chris Andrade**: He's willing to cut people out for us, guys.

[01:38:43] **Chris Andrade**: We're moving up the chain list.

[01:38:45] **Chris Andrade**: So we got the guys on the line, right?

[01:38:47] **Chris Andrade**: We went through scenarios.

[01:38:49] **Chris Andrade**: We did some stress testing.

[01:38:51] **Chris Andrade**: We think we're ready to...

[01:38:53] **Chris Andrade**: Trent said to allow his plug-in to be initiated if you want.

[01:38:59] **Chris Andrade**: Over the...

[01:39:01] **Chris Andrade**: So, I don't know how busy you are over the weekend, but I figured it'd be a good time to make sure things are working while it's on the slow time.

[01:39:10] **Chris Andrade**: No, I agree 100%, dude.

[01:39:12] **Chris Andrade**: I got time.

[01:39:13] **Chris Andrade**: Saturday, I'm going to be...

[01:39:22] **Chris Andrade**: Well, I think we were just wanting your approval so we could turn the switch on.

[01:39:31] **Trent Christopher**: Yeah, that's fine.

[01:39:32] **Chris Andrade**: Yeah, let's do it, dude.

[01:39:33] **Chris Andrade**: Tomorrow I have a church in the morning at 6-7.

[01:39:36] **Chris Andrade**: Yep.

[01:39:37] **Chris Andrade**: Then I'm going to go and meet up with a dude that I know that's building a coffee shop over there sometime, but I'll be free, dude.

[01:39:46] **Chris Andrade**: No, no.

[01:39:47] **Chris Andrade**: It's done.

[01:39:49] **Chris Andrade**: It's done.

[01:39:50] **Chris Andrade**: Bro, it's done.

[01:39:51] **Chris Andrade**: It's done.

[01:39:52] **Chris Andrade**: It's done.

[01:39:53] **Chris Andrade**: So you guys can start testing it over the weekend to start calling it and messing around and be like...

[01:39:59] **Chris Andrade**: Yeah,

[01:40:01] **Chris Andrade**: So, I don't know how busy you are over the weekend, but I figured it'd be a good time to make sure things are working while it's on the slow time.

[01:40:10] **Chris Andrade**: No, I agree 100%, dude.

[01:40:12] **Trent Christopher**: I got time.

[01:40:13] **Trent Christopher**: Saturday, I'm going to be...

[01:40:22] **Chris Andrade**: Well, I think we were just wanting your approval so we could turn the switch on.

[01:40:31] **Chris Andrade**: Yeah, that's fine.

[01:40:32] **Chris Andrade**: Yeah, let's do it, dude.

[01:40:33] **Chris Andrade**: Tomorrow I have a church in the morning at 6-7.

[01:40:36] **Chris Andrade**: Yep.

[01:40:37] **Trent Christopher**: Then I'm going to go and meet up with a dude that I know that's building a coffee shop over there sometime, but I'll be free, dude.

[01:40:46] **Chris Andrade**: No, no.

[01:40:47] **Chris Andrade**: It's done.

[01:40:49] **Chris Andrade**: It's done.

[01:40:50] **Chris Andrade**: Bro, it's done.

[01:40:51] **Chris Andrade**: It's done.

[01:40:52] **Chris Andrade**: It's done.

[01:40:53] **Trent Christopher**: So you guys can start testing it over the weekend to start calling it and messing around and be like...

[01:40:59] **Trent Christopher**: Yeah,

[01:41:00] **Chris Andrade**: So, you know, start testing it, break it, and like, hey, I'm Joe Smith from Flagstaff, Arizona, with these crazy, oh, my gosh, it's so funny, okay, well, so I don't, yeah, it looks like he's pushing buttons and stuff right now I'm looking at, like I'm seeing buttons getting pushed.

[01:41:31] **Chris Andrade**: Did you hear that, guys?

[01:41:33] **Chris Andrade**: No, I couldn't hear it.

[01:41:34] **Chris Andrade**: Is it going to catch the outbound calls, too?

[01:41:38] **Chris Andrade**: I think so.

[01:41:41] **Chris Andrade**: I don't see any reason why it wouldn't.

[01:41:43] **Chris Andrade**: It should be.

[01:41:45] **Chris Andrade**: Yeah, because right now, Jobber doesn't do anything with outbound calls.

[01:41:49] **Chris Andrade**: It only deals with inbound calls and a catcher, that's an opportunity.

[01:41:53] **Chris Andrade**: Got it, got it.

[01:41:54] **Trent Christopher**: No, it should be doing both inbound and outbound calls.

[01:41:57] **Trent Christopher**: areing I was getting outbound can't both some whhiritta

[01:42:00] **Chris Andrade**: That you guys were calling and leaving voicemails.

[01:42:06] **Chris Andrade**: Is there any more status updates on you heading out of town on Tuesday?

[01:42:18] **Chris Andrade**: I'm trying to push it further back in the week because I don't want to do it right in the middle of the week.

[01:42:23] **Chris Andrade**: I'm going to try and do Wednesday, Thursday, so I probably will stay here Monday, Tuesday and then leave super early Wednesday morning.

[01:42:31] **Chris Andrade**: I think that would be a good plan because maybe we could use it on Thursday.

[01:42:38] **Chris Andrade**: We'll have some instances where we can start showing Alyssa how to categorize these calls in a way that is easy and efficient for us to start figuring out how to kind of create a category system, right?

[01:42:52] **Chris Andrade**: Is that what it's called?

[01:42:54] **Chris Andrade**: We'll give her just an introduction on to what we're expecting her to do.

[01:42:57] **Chris Andrade**: That's all.

[01:42:58] **Chris Andrade**: Cool.

[01:42:59] **Chris Andrade**: Thank you.

[01:42:59] **Chris Andrade**: Thank you, актив remarks.

[01:42:59] **Chris Andrade**: you We'll You

[01:43:01] **Chris Andrade**: Um, do you guys, uh, you can just leave it.

[01:43:05] **Chris Andrade**: You can go.

[01:43:06] **Chris Andrade**: Yeah.

[01:43:08] **Chris Andrade**: Okay.

[01:43:08] **Trent Christopher**: I was talking to this guy on Quo, um, a minute ago and then Nikki called me and then she called me again.

[01:43:15] **Chris Andrade**: So I had to switch over from Quo to my cell phone and it, it held it and then it said swap it back.

[01:43:20] **Chris Andrade**: But when I went back into Quo, I couldn't figure out how to re, uh, well, he wasn't there when I came back, but I, but it was, he was on there, but I wasn't able to, uh, connect to him.

[01:43:33] **Chris Andrade**: said I was, so I'm just calling that place back up.

[01:43:35] **Chris Andrade**: Somebody actually answers or if he answers me right now, I want to talk to him real quick.

[01:43:39] **Chris Andrade**: Um, did you guys see the, um, I don't remember what I was doing.

[01:43:50] **Trent Christopher**: I was thinking it was really good too, but it's okay.

[01:43:54] **Trent Christopher**: Oh, well, you guys, we got our WhatsApp channel.

[01:43:57] **Chris Andrade**: Thank you very much.

[01:44:00] **Chris Andrade**: Did you see that message I sent you that said that one thing got approved but the other one hasn't and you recommitted or something?

[01:44:11] **Chris Andrade**: I'm looking at it now.

[01:44:16] **Chris Andrade**: Okay, there were four things in there and two weren't okay and two were okay and now three are okay but one's not okay.

[01:44:25] **Trent Christopher**: So you say some of them are okay but not all of them?

[01:44:30] **Trent Christopher**: Yeah, you said one.

[01:44:31] **Trent Christopher**: No, like there's four things holding up the transfer of the call and when I looked at it last time two of them were okay and two of them weren't okay and now three of them are okay and only one's not okay.

[01:44:43] **Trent Christopher**: thought I sent a screenshot of what wasn't okay to the WhatsApp thing but maybe I forgot to send it.

[01:44:50] **Trent Christopher**: Yeah, I'll have to go back and look and see and we got a lot of messages in here so I'm looking.

[01:44:57] **Chris Andrade**: Support called me responded back to me.

[01:44:59] **Chris Andrade**: you.

[01:44:59] **Trent Christopher**: Bye,,

[01:45:00] **Trent Christopher**: I can't remember how.

[01:45:01] **Trent Christopher**: I think I was doing a chat with them, actually, and I thought I took a screenshot of the chat and I sent it to you guys, but it was basically saying that it could take from 24 to 48 hours for it to go regardless.

[01:45:13] **Trent Christopher**: So I don't even think it's been that long, has it?

[01:45:17] **Trent Christopher**: It does say that typically it takes 24 to 48 hours for full SMS functionality to be restored.

[01:45:25] **Chris Andrade**: For now, please update your registration details as advised and monitor the situation.

[01:45:30] **Chris Andrade**: If you need further assistance, please reach out.

[01:45:33] **Chris Andrade**: But then what it says at the top here, it says it seems that your A2P registration status requires you to update your opt-in details and resubmit.

[01:45:46] **Chris Andrade**: But I thought there was a guy that was supposed to be taking care of that for you.

[01:45:53] **Chris Andrade**: Hey guys, I'm just going to get this guy's email address really quick and I'll be right back.

[01:45:57] **Chris Andrade**: Okay.

[01:45:57] **Chris Andrade**: Sure.

[01:45:58] **Chris Andrade**: Sure Thank so much.

[01:45:59] **Chris Andrade**: great.

[01:46:03] **Chris Andrade**: Hey, Chris, for some reason, sometimes I think he's talking and I can't hear him because, like, maybe the microphone is cutting it out or something, like it's trying to do noise suppression Yeah, let me text him and he, oh, you're right, it's probably what's happening Sometimes, like, he comes through just fine and then other times it's, like, completely dead silent Yeah, let me text him this link Hey, you guys have iPhone, right?

[01:46:30] **Chris Andrade**: Yeah, can you message him through iPhone this link?

[01:46:35] **Trent Christopher**: I'll give you his number to the personal number because I'm on my Windows and he doesn't know my Windows computer phone number Hey, Kelsey, we're going to send you a Google Meet link real quick because it's hard for them to hear you, okay?

[01:46:54] **Trent Christopher**: right?

[01:46:58] **Trent Christopher**: Oh, this is That's

[01:47:10] **Chris Andrade**: He is hustling right now.

[01:47:19] **Trent Christopher**: Let me know if you need the number to send Kelsey that link.

[01:47:26] **Trent Christopher**: Here, I can do that.

[01:47:28] **Trent Christopher**: Yeah, if you can do it.

[01:47:36] **Trent Christopher**: We're sending him the Google Meet link.

[01:47:38] **Trent Christopher**: Could we just send it in the WhatsApp?

[01:47:41] **Chris Andrade**: Oh, yeah.

[01:47:42] **Chris Andrade**: Bingo.

[01:47:43] **Chris Andrade**: Thank you, man.

[01:47:44] **Chris Andrade**: Stupid.

[01:47:45] **Chris Andrade**: So stupid.

[01:47:52] **Chris Andrade**: Thank you.

[01:47:53] **Chris Andrade**: That's anyways.

[01:47:56] **Chris Andrade**: Sorry.

[01:47:57] **Chris Andrade**: Thank you.

[01:47:58] **Chris Andrade**: you Thank you.

[01:47:59] **Chris Andrade**: Bye,

[01:48:04] **Trent Christopher**: Hey, Kelsey.

[01:48:05] **Trent Christopher**: Yeah, hey, open up.

[01:48:07] **Trent Christopher**: Can you open up WhatsApp and click on that, Lee?

[01:48:09] **Trent Christopher**: Because they're having a hard time hearing you because it's on the phone.

[01:48:14] **Trent Christopher**: Yeah.

[01:48:14] **Trent Christopher**: Oh, yeah.

[01:48:15] **Trent Christopher**: Where's my iPad?

[01:48:16] **Trent Christopher**: Hold on.

[01:48:20] **Chris Andrade**: It's in WhatsApp.

[01:48:22] **Chris Andrade**: Zaylor!

[01:48:23] **Trent Christopher**: That was close.

[01:48:25] **Trent Christopher**: can't get you up.

[01:48:30] **Trent Christopher**: What?

[01:48:36] **mytpix LLC**: Are more people talking to you?

[01:48:39] **mytpix LLC**: Can you join in on this conversation or what?

[01:48:42] **mytpix LLC**: Yeah, join in on that link and hang up with me.

[01:48:48] **mytpix LLC**: To your WhatsApp and the Flutter Mechanics WhatsApp?

[01:48:58] **mytpix LLC**: All right, he should be coming in.

[01:49:04] **Trent Christopher**: I got to admit him, hold on, I can find, where is he at, there he is.

[01:49:19] **mytpix LLC**: I hate when that happened.

[01:49:21] **mytpix LLC**: I know, I need to turn that off, setting off somehow.

[01:49:26] **mytpix LLC**: There we go.

[01:49:29] **mytpix LLC**: I made it.

[01:49:31] **mytpix LLC**: Hey, hey, hey.

[01:49:34] **Trent Christopher**: That sounds way better.

[01:49:35] **Trent Christopher**: Okay, now, yeah, I was hearing like, it was really bad before.

[01:49:37] **Trent Christopher**: This is way better.

[01:49:38] **mytpix LLC**: Okay, so earlier I had, what I was trying to say is I went into the, I was on the Quo app, and I went into there where it says it's not done yet, and I went to chat with the people, and then it got me to a spot where it says everything is cool except for this one thing.

[01:49:54] **mytpix LLC**: And I don't know if there's something we have to do, because nobody ever got back to me from support.

[01:49:58] **mytpix LLC**: Like the guy got back to me yesterday acting like he was going

[01:50:00] **mytpix LLC**: That helped me, but I haven't heard of  all day.

[01:50:01] **mytpix LLC**: So I don't know.

[01:50:02] **mytpix LLC**: He said he was going to fix it.

[01:50:03] **Chris Andrade**: He made me believe he was.

[01:50:05] **Chris Andrade**: Yeah, he did.

[01:50:05] **Chris Andrade**: I remember you sent me that message.

[01:50:07] **Chris Andrade**: Okay.

[01:50:08] **Chris Andrade**: I thought so.

[01:50:09] **Chris Andrade**: But you sent me the message saying where I read that he said he was going to, if you gave him authorization to go ahead and go in there and fix it, he would work on it for you.

[01:50:18] **mytpix LLC**: Yeah.

[01:50:18] **mytpix LLC**: Yeah.

[01:50:18] **Chris Andrade**: So I think I should just be patient, but it's really being a burden for me right now when people are texting me and I can't respond to them because I'm having to go to like, I'm not using my personal number, but I'm going over to Jobber.

[01:50:29] **Chris Andrade**: And I'm sending them a message, but they don't recognize that number.

[01:50:32] **Chris Andrade**: Right.

[01:50:32] **Chris Andrade**: Right.

[01:50:33] **Chris Andrade**: The only, the only other suggestion I'm going have is to call them instead of texting them when you have to reply back.

[01:50:38] **Chris Andrade**: But that sucks.

[01:50:39] **Chris Andrade**: I get it.

[01:50:39] **Trent Christopher**: Yeah.

[01:50:40] **Trent Christopher**: Yeah.

[01:50:40] **Trent Christopher**: No, it's okay.

[01:50:40] **Trent Christopher**: I just don't want it to be like that next week when I'm going out of town and everything else.

[01:50:43] **mytpix LLC**: So I'm just, I just wanted to make sure that there wasn't something we needed to do.

[01:50:47] **mytpix LLC**: I'm just saying that there were four things that were on there that need to happen.

[01:50:50] **Trent Christopher**: And two of them were grayed out yesterday.

[01:50:53] **Trent Christopher**: And after talking to that guy, only one's grayed out and it's the one on the bottom.

[01:50:56] **Trent Christopher**: I just, that's, that's, I just don't.

[01:51:00] **Trent Christopher**: I even how I got there, I would I would share with you voicemail to customers.

[01:51:05] **Trent Christopher**: Would it still pick up voicemails as he leaves them?

[01:51:11] **Trent Christopher**: What?

[01:51:12] **Trent Christopher**: If Kelsey left voicemails through Cleo, would it pick up the voicemail he leaves?

[01:51:19] **Trent Christopher**: Wait, who's leaving voicemails for who?

[01:51:22] **Trent Christopher**: If Kelsey, like he said right now, he's having to leave voicemail, or if we called and left a voicemail to the people that he can't send text messages to, would Cleo pick that up?

[01:51:33] **Trent Christopher**: Voicemail?

[01:51:35] **Trent Christopher**: I'll call, yeah.

[01:51:37] **Trent Christopher**: Okay.

[01:51:37] **Trent Christopher**: Yeah, it should be, they should be picking all that up.

[01:51:42] **Trent Christopher**: Yeah, we're gonna, I'm gonna test it over there.

[01:51:45] **Trent Christopher**: I'm excited to test that out, actually.

[01:51:47] **mytpix LLC**: Yeah, that's, that's, I've already made the switch.

[01:51:50] **mytpix LLC**: So, yeah, be able to, if you make phone calls, you should be able to see that.

[01:51:53] **Trent Christopher**: Now, it doesn't do messages right now.

[01:51:56] **Trent Christopher**: Yeah, I know.

[01:51:57] **Trent Christopher**: We haven't really figured out the exact.

[01:51:59] **Trent Christopher**: See.

[01:52:00] **Trent Christopher**: I'm of how to handle the messages right at the moment, but phone calls and contact updating and contact creation, if there's a new one going from your phone, if a call comes through, it's expected that it will take your Quo contact and it will create the new contact, but it prioritizes what's in Jobber.

[01:52:20] **mytpix LLC**: So if it's already in Jobber, it will prioritize what's there first, but if it's not in Jobber, it'll take whatever's in your phone and put it in there.

[01:52:28] **mytpix LLC**: Oh, nice.

[01:52:29] **mytpix LLC**: And then we can just fix the, fix the rest of it up.

[01:52:31] **mytpix LLC**: Yeah.

[01:52:32] **mytpix LLC**: And if, if either of those fail, like if for any reason, someone is totally new and you talk to them and you ask them their name and their phone number, we'll take their name and phone number and create the contact based on that.

[01:52:46] **Trent Christopher**: So if I get their company name and their address, will they add that stuff in there?

[01:52:50] **Trent Christopher**: Yes.

[01:52:50] **Trent Christopher**: Oh .

[01:52:53] **Trent Christopher**: Yeah.

[01:52:53] **Trent Christopher**: If you do, you do first name, last name, phone number, email, or address, it'll take any of that stuff and it'll.

[01:53:00] **Trent Christopher**: Now, it just needs to be, you know, obvious that it's an email.

[01:53:05] **Trent Christopher**: I mean, it should be relatively obvious and spelled correctly.

[01:53:10] **mytpix LLC**: So, well, like that guy from Apache, whatever this morning, I've been sharing like the process of how that calls me on today with you guys.

[01:53:17] **mytpix LLC**: Yeah.

[01:53:17] **mytpix LLC**: But like when I told him, hey, this is being recorded.

[01:53:20] **mytpix LLC**: I need you to give me all your information right now.

[01:53:22] **mytpix LLC**: So my secretary has it.

[01:53:24] **Trent Christopher**: He's like, he ratted it all off in one line.

[01:53:28] **Trent Christopher**: Like he already knew, you know what I mean?

[01:53:29] **Trent Christopher**: So I didn't even have to tell him.

[01:53:30] **Trent Christopher**: gave me his address, his phone, you know, like his email.

[01:53:33] **Trent Christopher**: He didn't, he didn't say the email, but I was like, I need your email too.

[01:53:36] **Trent Christopher**: And then he said it and that was it, you know?

[01:53:38] **Trent Christopher**: So that's awesome, bro.

[01:53:41] **Trent Christopher**: Yeah.

[01:53:41] **mytpix LLC**: So one thing I want to set expectations on real quick is that AI generally is not going to be 100% ever 100%.

[01:53:51] **mytpix LLC**: Okay.

[01:53:52] **mytpix LLC**: But it's going to get better and better as we continue to find things, errors and correct it.

[01:53:58] **Trent Christopher**: So in.

[01:54:00] **Trent Christopher**: In the beginning here, it's going to be mostly important to test it.

[01:54:04] **Trent Christopher**: And when we find things that aren't quite right, to note them down somehow.

[01:54:09] **Trent Christopher**: Yeah.

[01:54:10] **Trent Christopher**: Yeah.

[01:54:10] **Trent Christopher**: And like, it's a lot easier.

[01:54:12] **Trent Christopher**: It would be a lot easier.

[01:54:13] **Trent Christopher**: Like when Alyssa is talking to the customer to just verify the information she has over the phone with them, as opposed to going back and listening to the whole 20 minute conversation.

[01:54:22] **mytpix LLC**: Right.

[01:54:22] **mytpix LLC**: And that's what actually I should also have said was that what we'll need Alyssa to do is that when she gets this information, she cannot trust the information 100%.

[01:54:33] **mytpix LLC**: She needs to verify it, at least until we can build a certain level of trust in the system.

[01:54:39] **Trent Christopher**: She needs to go and look at the stuff like she would normally do.

[01:54:42] **Trent Christopher**: Yeah.

[01:54:42] **Trent Christopher**: And she understands.

[01:54:44] **Trent Christopher**: Yeah.

[01:54:44] **Trent Christopher**: I think that's going to be, you guys can tell her whatever you want to tell her and she'll write down notes and stuff like that.

[01:54:50] **Trent Christopher**: But I think she understands that it's not 100% just from the little bit of interaction that she's had with it.

[01:54:56] **mytpix LLC**: Yeah.

[01:54:56] **mytpix LLC**: It's not 100%.

[01:54:57] **mytpix LLC**: It just isn't.

[01:54:58] **mytpix LLC**: I mean, this is going to be.

[01:55:00] **mytpix LLC**: I better than what Quo's was, but at the same time, based on my testing it is, but at the same time, it's not going to be perfect.

[01:55:09] **mytpix LLC**: It has a lot to do with you have a voice and there can be a misinterpretation of a voice.

[01:55:15] **mytpix LLC**: It might be unclear.

[01:55:17] **mytpix LLC**: They speak broken languages.

[01:55:20] **mytpix LLC**: Yeah.

[01:55:21] **mytpix LLC**: Just people don't always speak straight.

[01:55:23] **mytpix LLC**: Correct.

[01:55:23] **mytpix LLC**: Right.

[01:55:24] **mytpix LLC**: So does the quality of my connection affect the or, or is that not affecting like when I'm hearing it choppy and breaking up, is that what Quo's getting to, or is Quo getting a cleaner copy of it?

[01:55:37] **mytpix LLC**: Um, it will probably still get some disruptions, but I'm not sure to what degree it may be improved than what you're hearing because you got two ways you're listening from someone and you're sending yours.

[01:55:53] **mytpix LLC**: So I don't know.

[01:55:54] **mytpix LLC**: I'm not sure.

[01:55:55] **mytpix LLC**: To be honest, I would expect it'll probably still be broken a little bit.

[01:55:58] **Trent Christopher**: I, I just got, um,

[01:56:00] **mytpix LLC**: Let me grab it here.

[01:56:02] **Trent Christopher**: I just got a list of this thing right here.

[01:56:04] **Trent Christopher**: Well, I told her to go to Amazon, pick out what she wanted to wear.

[01:56:06] **mytpix LLC**: Cause I don't, I'm not gonna be wearing it, but this hooks to her cell phone and to her computer.

[01:56:11] **Trent Christopher**: So like if she's walking, wandering around, then the phone rings, she can just tap this button and it picks up from the cell quo app.

[01:56:17] **Trent Christopher**: And if she's at her desk, then she just picks it up from the, you know, the thing that pops up right there.

[01:56:21] **Trent Christopher**: And we did some tests earlier with it and it was crystal clear with her sitting over here in the office.

[01:56:26] **Chris Andrade**: Yeah.

[01:56:27] **Trent Christopher**: You know, mine's going to have a little chop, but I'm, I'm fine with it.

[01:56:30] **mytpix LLC**: You know, like I'm okay with it because the, the good is way more than the bad.

[01:56:34] **mytpix LLC**: But for her in here, like when I was talking to her and even like wearing this, it's really nice to listen to.

[01:56:39] **mytpix LLC**: And then she can listen to the recordings real quick with this and it's not, you know, bothering everybody or whatever.

[01:56:45] **mytpix LLC**: So this is, I mean, this, I would have bought something a lot more expensive and not near this bulky, but that's just her, you know, she's frugal and she picked it out herself and she likes it.

[01:56:55] **mytpix LLC**: That's fine.

[01:56:56] **mytpix LLC**: Yeah.

[01:56:56] **mytpix LLC**: As long as she likes it, that's the most important thing.

[01:56:58] **mytpix LLC**: Cause she's the one wearing it.

[01:57:00] **mytpix LLC**: Yeah.

[01:57:01] **mytpix LLC**: She doesn't have to wear it, but it's to make her life easier, hopefully.

[01:57:04] **mytpix LLC**: Well, exactly.

[01:57:04] **mytpix LLC**: Her hands are free.

[01:57:05] **mytpix LLC**: She doesn't have to.

[01:57:06] **mytpix LLC**: Yeah.

[01:57:07] **mytpix LLC**: No, no, that's good.

[01:57:08] **mytpix LLC**: Exactly.

[01:57:09] **mytpix LLC**: And hopefully we'll be able to feed this information into her.

[01:57:13] **mytpix LLC**: And I think that you'll be much happier with this integration than what the previous one was.

[01:57:20] **mytpix LLC**: Oh, yeah.

[01:57:21] **mytpix LLC**: I can imagine.

[01:57:22] **mytpix LLC**: I've already sent you screenshots and stuff, so it's what I sent you.

[01:57:27] **mytpix LLC**: Yeah, yeah.

[01:57:28] **mytpix LLC**: I haven't seen them yet.

[01:57:30] **mytpix LLC**: I've been just going all over today, but it's good.

[01:57:32] **mytpix LLC**: It's exciting.

[01:57:33] **mytpix LLC**: I got everything lined up.

[01:57:34] **mytpix LLC**: We got everything.

[01:57:35] **mytpix LLC**: Me and Andrew put that quote together for that client that we had, and we kind of developed a process.

[01:57:43] **mytpix LLC**: We already have a template now, so the next time we can just modify it and send it.

[01:57:46] **mytpix LLC**: And yeah, we did a lot of brainstorming, so we're going to just continue to hone that in.

[01:57:52] **mytpix LLC**: But he's super smart, bro.

[01:57:53] **mytpix LLC**: Like when it comes to like selling and like residual income, and he just has ideas like,

[01:58:00] **mytpix LLC**: You know, I'm like, you were talking about service contracts.

[01:58:02] **mytpix LLC**: And I'm like, well, what are we going to do with the person that's in Flagstaff or in wherever, you know, because I don't want to sell them the contract at the same price as the other one.

[01:58:11] **mytpix LLC**: He's like, all we got to do is just write in the service contracts and say, this includes two hours of travel or whatever you want to say.

[01:58:16] **mytpix LLC**: And then anything else over that is just going to be an additional trip charge to get us out there.

[01:58:21] **mytpix LLC**: But then there's not a bunch of labor and stuff, you know?

[01:58:23] **mytpix LLC**: So like, like, for instance, like this job that I got, because we were going over this one, it's a five hour drive.

[01:58:29] **mytpix LLC**: I'm like, bro, Joe, if it's a five hour drive, and I got to go out there, I got to pay Joe 200 bucks to drive over there.

[01:58:36] **mytpix LLC**: I lost 200 bucks.

[01:58:37] **mytpix LLC**: But if they pay me my travel charge, then I bill them 300 for the travel or, you know, whatever, at least it pays for his day.

[01:58:43] **mytpix LLC**: Or, you know, I'm not losing money that day or something.

[01:58:46] **mytpix LLC**: I'm doing other things making money over here.

[01:58:48] **mytpix LLC**: But I do like his approach of because he wants to close the sale and get the money up front, you know, like being.

[01:58:55] **mytpix LLC**: But we talked about doing like month to month things because and he said, dude, everything.

[01:59:00] **mytpix LLC**: Every one of these is going to have to be handcrafted because you got to look at the potential, you know, you can't be like, like Alyssa's trying to get me to sell somebody a service contract, like people call me and inquire, they're like, we want to get a service contract and Alyssa, like, she takes that as a, an opportunity when they have a latex printer that's eight years old.

[01:59:18] **Trent Christopher**: And I'm like, I don't want no service contract on a latex printer eight years old.

[01:59:21] **Trent Christopher**: Like, hell no.

[01:59:22] **Trent Christopher**: I mean, just give my phone number and tell me to call me when it breaks.

[01:59:24] **Trent Christopher**: Like, that's not good.

[01:59:25] **Trent Christopher**: That's not a good deal for me, you know, but yeah, but she doesn't know the difference where Andrew would know.

[01:59:30] **Trent Christopher**: Or, or, or she might try and sell somebody a contract when we've, we've done $10,000 worth of labor on their printer in the last year.

[01:59:37] **Trent Christopher**: Yeah.

[01:59:37] **mytpix LLC**: So like every, you know, so every opportunity kind of needs to be handheld and not, not everyone, like a lot of it can be automated, but when it comes to the actual, like the selling of a piece of equipment, like that's got it, that takes a hand touch, you know, and you, and if you can have that rapport with the customer on the phone and I can like set Andrew up for the followup the way it is, he could talk the talk and do all that.

[02:00:00] **Trent Christopher**: And so, and I'm sure there's a way we can track the opportunities that we work together on because I want to see how lucrative it is because everything I'm giving him is things I wasn't going to do anyways.

[02:00:12] **mytpix LLC**: Yeah.

[02:00:13] **Trent Christopher**: Yeah.

[02:00:13] **Trent Christopher**: Right on.

[02:00:14] **Trent Christopher**: Right on.

[02:00:14] **Trent Christopher**: So I'm actually probably going to jump off here.

[02:00:17] **mytpix LLC**: Yeah, me too.

[02:00:18] **mytpix LLC**: But I just wanted to make sure that you knew that we were going to transition this.

[02:00:22] **mytpix LLC**: So over the weekend, if you want to test it.

[02:00:25] **mytpix LLC**: Oh, I do.

[02:00:25] **mytpix LLC**: If you see something that's like totally glaring, like, whoa, I don't want that at all.

[02:00:29] **mytpix LLC**: You know, let us know as soon as possible and then we can flip it off and we can, it's an easy switch to go back to the way it was before.

[02:00:36] **mytpix LLC**: We'll do it tomorrow, Chris.

[02:00:37] **mytpix LLC**: When, after we get done meeting up, we'll, we'll, practice a couple of times and you can be the customer and I can be the vendor and we'll go back and forth with a couple of different situations because I know what kind of questions people ask.

[02:00:47] **mytpix LLC**: And both Matthew and I can support the switch back over to fall back to what it was or it shouldn't be an issue with, you know, supporting tomorrow.

[02:00:56] **mytpix LLC**: I'm busy with some family stuff, but I'll have my laptop if some.

[02:01:07] **Chris Andrade**: I appreciate your time there, Kelsey.

[02:01:11] **mytpix LLC**: Thank you.

[02:01:14] **Chris Andrade**: Just check it out and see what you think.

[02:01:16] **Chris Andrade**: I got Gus, my neighbor that does the printing wrap thing next door.

[02:01:24] **Chris Andrade**: Him and Joe are collaborating right now to wrap Joe's car.

[02:01:27] **Chris Andrade**: So I already got the artwork set up, but I got Joe over here.

[02:01:31] **mytpix LLC**: I got Gus over here.

[02:01:32] **Trent Christopher**: I kind of gave him a little gist of what we're talking about.

[02:01:35] **mytpix LLC**: Yeah.

[02:01:36] **mytpix LLC**: And I gave him the whole rundown.

[02:01:37] **mytpix LLC**: I'm like, look, cause I want Gus.

[02:01:39] **mytpix LLC**: Like I like Gus.

[02:01:39] **mytpix LLC**: He started a business, but he's struggling, dude, to get leads and stuff.

[02:01:45] **mytpix LLC**: Cause we were in a  neighborhood, dude.

[02:01:47] **mytpix LLC**: Like we're in the shittiest part of town and he's wrapping cars and doing things like that.

[02:01:50] **mytpix LLC**: If he was in Scottsdale, he'd be busy as .

