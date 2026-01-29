# Trevor Meeting - December 2, 2025

## Meeting Details
- **Date:** December 2, 2025
- **Client:** Trevor (Idea Framework Website)
- **Project Phase:** Phase 2 Implementation

## Transcript

Review Phase 2 IDEA Framework Website Updates - December 02
VIEW RECORDING - 58 mins (No highlights): https://fathom.video/share/EcdijzxNSsAkTbTN5hJPspJx2WPqho33

---

0:00 - Matthew Kerns (12kernsmatthew@gmail.com)
  Hey Trevor, good morning. For some reason I can't hear you. I think I see you're on mute.

0:31 - Trevor Bradford (Brandvoice)
  Can you hear me now, Matt? Yep.

0:34 - Matthew Kerns (12kernsmatthew@gmail.com)
  Great stuff, okay.

0:36 - Trevor Bradford (Brandvoice)
  Cool, cool, cool.

0:40 - Matthew Kerns (12kernsmatthew@gmail.com)
  Okay, so I've made some updates today. Close to fixing one last issue, but I think, yeah, just wanted to hear what your thoughts on what I showed yesterday.  Thank

1:00 - Trevor Bradford (Brandvoice)
  I thought it was great progress. It's terrific. I've got some tasks to do at my end regarding video hosting.  I've not finalized that yet. I think Vimeo is probably going to be the way. But before I sign up for something else, I just want to make sure that I don't have that facility at Mastermind.  And although I'm not clear about how to make it work on Mastermind, I've got a support ticket open. I'm just willing to hear back from them.  I should hear probably today. So we'll get that result pretty quickly. So did you want to kick off and take it from you and then I'll chime in?

1:43 - Matthew Kerns (12kernsmatthew@gmail.com)
  Sure. OK, so, yeah, I think from what I've seen so far, at least I think I shared with you already, but the Vimeo might be a good one.  I think it's free. And then. So. I'll just kind of walk through. Here, let me share my screen first.  Yeah, I'll walk through updates since the last one I shared with you.

2:15 - Trevor Bradford (Brandvoice)
  So can you see? Matt, are you recording on Fathom on this one?

2:22 - Matthew Kerns (12kernsmatthew@gmail.com)
  Yes. You got it.

2:24 - Trevor Bradford (Brandvoice)
  Okay. I don't mind. Notetaker doesn't work on Google. So that's great. We've got notes. Okay, cool.

2:31 - Matthew Kerns (12kernsmatthew@gmail.com)
  Yeah. It's like 95% success rate. So everyone's not at But let me click through this because I was working on this part.
  ACTION ITEM: Fix minimized-state sign-in/logout; add logging; fix chatbot headings; push to Lovable for Trevor review - WATCH: https://fathom.video/share/EcdijzxNSsAkTbTN5hJPspJx2WPqho33?timestamp=157.9999  Okay, it looks like there's not a sign-in option when the thing is minimized. But I mean logout option there.  But we'll follow up on that. logout So what I have adjusted since last time is basically when you click through here, the last video I sent you, it had on the subscribe page, it had like this assessment component at the top that was not the one that we used.  So what I've done is now, so I think this copy might have been updated a little bit, then you sign in and now this page shows.  So, but yeah, I kind of skipped over the earlier part, but basically, and then this shows up here, so diagnostic results have been synced to your account after, once you're on the subscribe page, which I think is a good, nice touch.  And then before. before. We did see the diagnostic results now showing. So that was kind of the update there.  Do you want me to go back, or did you notice that already? I kind of went over it quickly.  If you would, please. OK, sure. Yeah, sorry. So diagnostic, click through here. So this is not signed in, right?  And here's the results. So this is the update. So before, it would just go to the subscribe page on the last loom that I sent you.  And it would show the diagnostic results at the top. Not like this, though.

4:51 - Trevor Bradford (Brandvoice)
  OK. So then, yeah.

4:56 - Matthew Kerns (12kernsmatthew@gmail.com)
  So now we sign in and. And here I do want to check, because I think, yeah, there's some error happening, where the, so it's getting stored to the database, but it's not being stored to, I'm just going to to do this, also logs here, and then this is the, so I can just do this quickly, but, should have more, more logs in here, potentially, because JSON, okay, so, that, I just wanted to update that, because, right now, it's, it's being stored in the database, but it's not being stored for the chat pod, the embed,  Headings don't get stored properly for the chatbot, so just working through that should potentially be a quick fix. But now we're here, right?  So there might be some updates we want to make here, but I just want to show you what happens next.  So for right now, we're just doing like the click through experience. So we don't have any payment set up yet.  I think this is what we wanted for this phase. So any of these buttons should be able to. haven't tested this one yet.  Okay, so that worked. Just click through and we're signed in and we can go to any of the pages and should have this stuff that I put in here.  Yeah, so that was the update since last time. That's all I did since the looms. Great.

7:02 - Trevor Bradford (Brandvoice)
  So is there a URL that I can use to access this version, Matt? Because obviously the one on Livable, it isn't current, is it?  Right. So I can just check the functionality and just make sure that all the copy is actually right. I mean, I spotted something that I'm probably going to want to change on the setup fee text.  I think I'll probably find a different way to say it, but that kind of thing. So I can just work through the flow myself and just experience it.

7:41 - Matthew Kerns (12kernsmatthew@gmail.com)
  Okay. Yeah, I can get that set up. Right now it's only on my local machine. Yeah. But what I can do, I think I can set up a, basically another environment, another Livable project, might be what I do.  tell Yeah. you. Um, or it might be another solution. I need to figure that out. Um, I think for now you can reference the Fathom video until I get that working, but I might be able to do it quickly.  If we, if our call doesn't go too far, I have till 6am so I can work on that. Or we can also go through it right now, but I know you, I get that you want to work through it and experience it and get there.  Right. So I can get this.

8:32 - Trevor Bradford (Brandvoice)
  Let's do it that way around so that then I can give you any, any texts and it's all in one hip.  So we're not going back and forth and messing around with it. Um, I, I had a thought the other, uh, last night, actually, uh, I'm in the middle of, uh, an outreach campaign via LinkedIn.  Uh, we're doing email and I've just started my BA on doing LinkedIn outreach nice. Nice. Nice. Nice.

9:00 - Matthew Kerns (12kernsmatthew@gmail.com)
  Navigator.

9:00 - Trevor Bradford (Brandvoice)
  And I've put together five different messages that we're going to test, and she's going to get salted on that.  And one of the things that I'd like to do when we're ready is put the link to the diagnostic in there.  So what I'm thinking is that because we've got two separate sales channels, one that we're working on here is to sell and market the app.  So obviously, the diagnostic is linked to the app, and there's the upsell. But via LinkedIn, that's a direct pitch by consultancy clients.  So obviously, I don't want to link them to the app. I want them to work with me directly. So would it be a simple job just to duplicate the code for the diagnostic part, stick it on Lovable as a separate project so it's just diagnostic that does simple data capture and a link to my calendar?  Calendly. Would that be a big job? Calendly.

10:01 - Matthew Kerns (12kernsmatthew@gmail.com)
  I feel like it's simple enough. In terms of time it would actually take to deploy and get it set up with an actual, on the actual URL.  I'm not sure how the domain part would work, because... I could just set up a new domain if that makes life easier.

10:27 - Trevor Bradford (Brandvoice)
  Okay. Yeah, because the Brand Coach app, it's specific to selling the app. But the brand consultancy service, although you can access that via the app if you want to, you can sign up for a meeting with me.  It's a slightly different thing. So what I would like to do is be able to have the diagnostic as just a standalone leader magnet.  So it's the same diagnostic that's attached to the front end of the full app. And... And... ... ... They both work the same way, they get people into a funnel, by offering them value, but what it is they're buying is potentially two separate offers.

11:12 - Matthew Kerns (12kernsmatthew@gmail.com)
  Okay, yeah, I think, so I haven't hooked up the domain to a lovable project before, but I have hooked up domains to projects, so I should be able to work through it.  It seems like you've already done that, or you did it.

11:34 - Trevor Bradford (Brandvoice)
  It's not difficult, I can't remember step by step exactly how it is, but you guided through with lovable anyway, it's really easy.  As part of a new project setup, you link it to a domain, and then my expectation of my limited experience of this would be just to copy code and put it into the new project, and you probably need to do some kind of cutoff inside the coding.  S. you. Thank Uh, because it won't exist at the moment, just to direct people to just sign up and get their diagnostic.  Yeah. And, and get a book a meeting with me, but for the LinkedIn side of things. Okay.

12:15 - Matthew Kerns (12kernsmatthew@gmail.com)
  So it'll be, so it'll be diagnostic the way it is. And then instead of signing in to the app, it would, it would direct to a Calendly page.  Yeah. Or do you want another page before the calendar link?

12:30 - Trevor Bradford (Brandvoice)
  Like a data capture page, Matt, please, where in order to download their report, they give me their email, their, their name and email address so that then I can get into a loop of email marketing if they don't sign up for a Calendly conversation.

12:48 - Matthew Kerns (12kernsmatthew@gmail.com)
  Yeah. So we might reuse the existing page with the results. And then instead of sign up, sign in, we say something else like, um, you may.  Yeah, so then, say book a meeting, and then when they click book a meeting, they, well, I mean, Calendly has an email field that they need to provide, right?  Yeah, maybe instead of adding another component, we can simplify and just book a meeting directs to the calendar link, and then you can get the emails from there.  Yes, that's possible.

13:34 - Trevor Bradford (Brandvoice)
  However, not everybody who wants the diagnostic necessarily wants a meeting at that moment. So I want to be able to give them their diagnostic, capture their data, and if they don't want to sign up, and if as far as they're concerned, that's great.  I had some value, but I don't want anything else, and I can put them in an email loop where we can market to them because they've showed interest that I know that they've got.  Some kind of brand issue, so I know that they're warm prospects because they wanted the diagnostic and then I can market to those guys, where there will be potentially a smaller proportion who would like to chat straight away, in which case they can book a meeting, and that link would come to Calendly, and that is probably the end of the funnel on that for LinkedIn, it's just a simple diagnostic, get your download, you share your data, that's it, or you go one step further and you book a meeting.

14:35 - Matthew Kerns (12kernsmatthew@gmail.com)
  Okay, and then I'm just thinking for the download PDF button, we could also include the email capture there, or do you want them to be able to directly download the PDF without email capture?

14:49 - Trevor Bradford (Brandvoice)
  I'd like to be able to get their data from the download. Now, it's pain in the  for them to have to input their data twice, I guess, on the Calendly page.  But I don't see a around that.

15:04 - Matthew Kerns (12kernsmatthew@gmail.com)
  Yeah, I think that would be okay. But we should not have them need to put it in twice if they download, and then they put their email in there, and then get access to the download, and then they decide, okay, I want to book a meeting.  We shouldn't show the capture email page again there, right? If we already have their email, then it should go directly.

15:29 - Trevor Bradford (Brandvoice)
  That would be great. But if that's a lot of coding and a lot of extra work, you know, for right now, you know, they've had something for free, and they want to book a meeting.  Well, it's not unusual to have to do it twice, I suppose, if you're on two separate platforms, one Calendly and one via Diagnostic.

15:48 - Matthew Kerns (12kernsmatthew@gmail.com)
  Oh, yeah, no, I meant like, when we're on that page, on the results page, if we hit download, then it shows the capture, email, and then they put it in.  let's And then they hit download, then they're on the page again, and they decide to book a meeting, then when they hit book a meeting, they should direct get directed to the Calendly link directly, instead of needing to input, because I think if they don't hit the download button, then and they just hit book a meeting, then you want to email capture first before the Calendly link, or is that?

16:26 - Trevor Bradford (Brandvoice)
  Yeah, I think so, because not everybody is going to book a meeting link, I mean, if you could enter a video in there as well, on that page, with me saying, hey, great, you've downloaded your link, if you'd like to talk to me one-on-one to get even more value, book a link below, and that's a call to actually, you know, direct, face-to-face video of the quality that I've shown you.

16:51 - Matthew Kerns (12kernsmatthew@gmail.com)
  So, okay, so would that be, would that be a component that's on the results page, no matter what, or only if they click the PDF download?

17:00 - Trevor Bradford (Brandvoice)
  I think we should have it on the results page anyway, and actually say, get your download below, and then would it be a separate message?  I don't want them to feel that they've got to have a meeting with me to get their download, because I would like to data capture them.  So, I think what it is, there's plenty of incentive for them to do the download anyway without the video.  When they've downloaded, on a kind of thank you page, that's page two in the funnel probably, after the diagnostic, there'll be a book a meeting and a video.  Me saying, hey, thanks, this is great. I hope they get great value from this, but I can really do blah, blah, blah.  You know, why don't we have a conversation?

17:54 - Matthew Kerns (12kernsmatthew@gmail.com)
  Yeah.

17:55 - Trevor Bradford (Brandvoice)
  And call them to actually to just book the meeting.

17:59 - Matthew Kerns (12kernsmatthew@gmail.com)
  Okay. So that would be a new page after they download the PDF, basically.

18:06 - Trevor Bradford (Brandvoice)
  Yeah, I mean, if you want, I could map it out as a new project in Lovable and start from scratch and see what it gives us.  Because I know you've got a lot to do. You've got to do your move. You know, you're doing the project for me at mates rates.  You know, don't want to load extra work onto you. And so I'd like to help as much as I possibly can.  So would that be, would that be a good idea? How do I tell, can Lovable look between projects, do you know?

18:40 - Matthew Kerns (12kernsmatthew@gmail.com)
  Yeah, I mean, you can duplicate a project. So what you can do is you can duplicate it and you can tell it basically once you're in the new project.  Like, I only want this component and here's what I want to do with it. And you explain everything. Uh, then, and then.  You can start setting up the flow, and we can see what we get from that. You can even say, like, delete everything.  Like, once you're in the new project, you can say, you can do whatever you want. Say, delete everything except this page, and then start building the next page.  The video component you might want to keep. Although, the video component, I haven't pushed it yet, because that's part of the Phase 2 branch deliverables, so that component won't be there.

19:39 - Trevor Bradford (Brandvoice)
  But this is all local on your machine at the moment, isn't it? So, the latest version isn't on lovable for me to duplicate.  Right.

19:51 - Matthew Kerns (12kernsmatthew@gmail.com)
  But the, yeah, so the video component, though, I think is the only piece missing, because the other one, the other.  The earlier diagnostic and results component is there. It won't have updated copy if there's updated copy. But, you know, that would be quick enough to adjust.  What I'm is also we need to... So the Phase 2 deliverables, I think we should cut those off at some point.  And then, like, the Phase 3, the next phase, we can be adding in the new features and I can include this as part of that as well.  Or like what you said, I mean, if we can make progress more quickly with you duplicating and doing it that way.  Basically, as soon as the payment is sent for the Phase 2... ... ... ... Then I can push to lovable, and then that can be available, and you can duplicate there.  I just don't know if that's necessary for the marketing campaign that you're trying to do, because there's not that many updates, except for the video component itself, which you could ask if it could be done, and it might just do it pretty easily.

21:22 - Trevor Bradford (Brandvoice)
  Yeah, if I ask it to embed a Vimeo player on the page, then it should just want a URL from Vimeo to pull the upload and play it, I would think.  Let me have a go, man. You continue doing what it is you've got to do for us to get to the end of Phase 2.  Send me an invoice, by the way. We'll get that sorted out. I don't keep hanging around for that. So that my objective is, app first, let's get that ready for beta, so that I can put it out there into...  The network, get some people testing it, get some feedback for any any final minor tweaks and just get marketing the damn thing, because I've been hanging around with it for such a long time.  I'm going to stop and start. It's been it's been a long, long process. So I really need to get that going.  And then in parallel with that, I'll do a duplicate of the project in Lovable. I'm competent enough to tell it what I want and explain what it what I need, at least in terms of the page flow.  And it might mean then that I just need a bit of help from you just to make sure it's joined at the back.  Yeah, it's really quite simple, confident what you're doing with the app. You know, I don't it doesn't need to have any memory or anything like that.  It just needs to offer a download. Once downloads done, it doesn't hold the memory. Customers got their document. That's great.  So they got their value in return for the data. said inhoe mic. a tends I put a video message there to them and said, hey, look, obviously you feel you've got an issue.  Why don't we have a conversation? I'm sure I can help you. No obligation, chat, blah, blah, blah. Sign up here at Calendly.  And then that's it. And that to me, I think, seems simple enough for Lovable to basically do it without  it all up like you did last time.

23:23 - Matthew Kerns (12kernsmatthew@gmail.com)
  Yeah, I think so. And then I'm sure.

23:29 - Trevor Bradford (Brandvoice)
  And then you can tell me what do you think it's good or bad or indifferent from your expertise point of view and something to work with.  Sounds good.

23:41 - Matthew Kerns (12kernsmatthew@gmail.com)
  Sounds like a plan. OK, yeah, I think the phase two deliverables are almost there. I just wanted to literally just confirm this last thing, and then I did want to review our meeting notes and make sure that I captured everything.  last slide. that to And had I I So as far as the invoice goes, essentially it's taking some time for it to process and get to my account.  I can see that you paid the invoice or the payment link. I think it was the payment link. So I can see that it's there, but they're just, they're holding on to the funds for a few days.  Yeah, I think, I think it's just cause it's kind of a new account with them. So they're like, they're, they're waiting a bit.  So, but, uh, what I was thinking and can I help it anyway?

24:42 - Trevor Bradford (Brandvoice)
  Can I help that in any way? I don't think so.

24:46 - Matthew Kerns (12kernsmatthew@gmail.com)
  I think it's just part of their process, um, for that first one that's already gone through, but what I was thinking is for the next one, we could potentially just do like a Zelle payment.  Um, and then I'd get it right. Okay, what's Zelle?

25:02 - Trevor Bradford (Brandvoice)
  I haven't used Zelle before.

25:04 - Matthew Kerns (12kernsmatthew@gmail.com)
  Okay, it's a payment. So basically, I have signed up with my phone number and email, but it's spelled Z-E-L-L-E.  And I think it was pretty easy to set up. Hopefully, they don't do a first-time delay from your end there, but I wouldn't think so.

25:31 - Trevor Bradford (Brandvoice)
  All right, I'll explore that, Matt.

25:33 - Matthew Kerns (12kernsmatthew@gmail.com)
  Okay, thank you. Yeah, that would be great. And then what we can do is, once you send that through, so I'll send you my phone number.  Well, I think you have my phone number from WhatsApp. So it's the same phone number that I used to send it with Zelle.  And then what we can do is, once that's sent through, I can push my updates to Lovable. a phone number.  It's get So we could potentially do that pretty quickly, like within the hour or the next couple hours, and then any updates that need to be made for fixing the Phase 2 deliverables, I can do and just push them, because the payment's already been made, right?  So that would allow you to duplicate the existing one when you set up the new project, if you want to do it that way.  Okay, cool.

26:31 - Trevor Bradford (Brandvoice)
  Let's do that.

26:34 - Matthew Kerns (12kernsmatthew@gmail.com)
  Okay, sounds good. And then I'll make sure and go in and just review our meeting notes and make sure everything is captured.  But I think I've done a good enough job where most of the stuff should be. I do need to confirm like, a couple of things, but I can go in and update and then that way you can go through the  And then, like new feature stuff, we can add, we can do like a phase three if you think that's necessary.

27:16 - Trevor Bradford (Brandvoice)
  Okay, well, I'll wait on the feedback on the beta just to see if people feel there's anything missing. I'd really like to try and get it out into the market as quick as possible and test it.  Yep. See what happens before we start adding stuff to it. Cool. I'm just looking for your invoice, Matt. Yeah, so as I code my business, wasn't it?  Okay. So, are you going to send me a second invoice?

27:48 - Matthew Kerns (12kernsmatthew@gmail.com)
  So, I would prefer to send you the Zelle. I'm not sure if there would be an invoice attached to that.  I want to... I want want wonder if I can just do an invoice that, or do a retroactive invoice that doesn't require like payment through that invoice.  Sure. just now.

28:12 - Trevor Bradford (Brandvoice)
  Or a receipt, it's just something for the accountant, that's all, you know, to track the payments.

28:19 - Matthew Kerns (12kernsmatthew@gmail.com)
  Yeah.

28:19 - Trevor Bradford (Brandvoice)
  So if you send me a link to your Zelle account, it will probably require me to create one as well.

28:25 - Matthew Kerns (12kernsmatthew@gmail.com)
  Okay.

28:25 - Trevor Bradford (Brandvoice)
  So let's do it, and I'll take care of that now. Okay.

28:30 - Matthew Kerns (12kernsmatthew@gmail.com)
  Sounds good. I think I can, let's see, if I do request. Yeah, Zelle has been nice. It's just, it won't be directly through my business, but I can just tell accounting later.  Let's see, add. Should I, I think I can just grab your phone number. Hopefully there's not within the. I've only used this with U.S.  people before, let me see, okay, plus four, seven, nine, six, six, two, eight, four, one, two, nine, okay. I think I'll use your email also, so trevor.bradford, I think?

29:40 - Trevor Bradford (Brandvoice)
  Yep, it's brandavoyce.co.uk. Okay. I'm on the Zelle page, I can't tell from this whether it's just for American businesses, well, I've got an American, well, this is a U.K.  business that we've put in this project through, so Well, let's try it, Matt.

30:04 - Matthew Kerns (12kernsmatthew@gmail.com)
  Yeah. Okay. Yeah. I'm setting up the request right now.

30:08 - Trevor Bradford (Brandvoice)
  Send it to me and we'll try it now.

30:13 - Matthew Kerns (12kernsmatthew@gmail.com)
  Okay. Brand. I know you sent me your business name. Here it is. Okay. I just want to do add as business on the Zelle side.  Yeah. In case that helps. Okay. Must be enrolled to receive money with Zelle, but that might prompt you to enroll.  Okay. Continue. Oh. Okay. Sorry. Just a little typo. Fixed it. Okay. Name. Doesn't For now, You Okay, let's put as the memo, Phase 2, Idea Framework Website.  Okay, I just sent the request, so hopefully you get an email.

31:24 - Trevor Bradford (Brandvoice)
  Should be with me in a second or two, I think.

31:30 - Matthew Kerns (12kernsmatthew@gmail.com)
  Okay, or a text message maybe too.

31:38 - Trevor Bradford (Brandvoice)
  See if it's coming to the junk.

31:54 - Matthew Kerns (12kernsmatthew@gmail.com)
  Okay. Okay. Thank you. It says must Brandvoice Retail must enroll this email address in Zill.

32:13 - Trevor Bradford (Brandvoice)
  Okay. Let's give that a go then. Okay. Let me share my screen, Matt. Okay. Maybe I'm being a bit dumb, but it's not particularly user friendly.  So here we are on the Zill page. Small business. Yep.

33:06 - Matthew Kerns (12kernsmatthew@gmail.com)
  Okay, so nothing happens there, I wonder if you, is there anywhere that, where you can enroll, like maybe under personal, and then you can mark it as business later, not sure.

33:22 - Trevor Bradford (Brandvoice)
  Let's try that, get started. I think I can't see your screen anymore.

33:31 - Matthew Kerns (12kernsmatthew@gmail.com)
  It's just showing small business highlighted on the Zelle home page. Okay. I'm if it froze.

33:44 - Trevor Bradford (Brandvoice)
  It started with Zelle. Sure. Okay, there we are. And here you're back. Thank you.

34:06 - Matthew Kerns (12kernsmatthew@gmail.com)
  I think there's a link down there that showed up right under beautiful lists. Yeah, that's not my bank.

34:14 - Trevor Bradford (Brandvoice)
  I'm in the UK. Okay.

34:17 - Matthew Kerns (12kernsmatthew@gmail.com)
  So I think it's UK only, Matt, by the look of it, based on that.

34:22 - Trevor Bradford (Brandvoice)
  Yeah.

34:31 - Matthew Kerns (12kernsmatthew@gmail.com)
  So requires US bank account. Okay. Yeah. Okay.

34:36 - Trevor Bradford (Brandvoice)
  All right.

34:38 - Matthew Kerns (12kernsmatthew@gmail.com)
  I'm not really sure another way to get paid instantly. So maybe we'll need to go the invoice route again, which is fine.  So there's another way. I'm just trying to think quickly if there's another way.

34:57 - Trevor Bradford (Brandvoice)
  Well, there's PayPal, but they charge lots of fees. guys. No Bye, Did you go to PayPal?

35:03 - Matthew Kerns (12kernsmatthew@gmail.com)
  Yeah, you could do PayPal. Let's have a look at PayPal.

35:09 - Trevor Bradford (Brandvoice)
  Okay.

35:14 - Matthew Kerns (12kernsmatthew@gmail.com)
  Yeah, sorry about that. I guess now we know.

35:22 - Trevor Bradford (Brandvoice)
  I'm going to log in. Yeah, that's the correct account.

35:48 - Matthew Kerns (12kernsmatthew@gmail.com)
  So is it yours, the same email for PayPal? Yeah, just getting my text.

35:54 - Trevor Bradford (Brandvoice)
  to Text. Text. Text. Okay, so I'm logged in.

36:16 - Matthew Kerns (12kernsmatthew@gmail.com)
  Okay, I've just requested it through PayPal now.

36:21 - Trevor Bradford (Brandvoice)
  Okay. Let's see. So there should be a request for payment in there somewhere.

36:50 - Matthew Kerns (12kernsmatthew@gmail.com)
  Brandvoice Retail, yep. Should be. Check my email.

36:56 - Trevor Bradford (Brandvoice)
  Yeah, is, yes, that's right, Brandvoice Retail Limited. Thank you. Thank Yeah.

37:03 - Matthew Kerns (12kernsmatthew@gmail.com)
  That's what I saw on my end as well. There we go. got a money request.

37:33 - Trevor Bradford (Brandvoice)
  Yes. So $500, pay now. Yeah, that's good. All right. Send. So, are you seeing this, on your side? No.  Okay. It's given me. It's it's confirmed it's sent money to you. Okay.

38:07 - Matthew Kerns (12kernsmatthew@gmail.com)
  Yep. All right. Yeah, there are some fees. Okay. Yeah, thank you. Okay, so I'll, I'll push the updates. I think I can do that very quickly.  So and then I can debug after you know, what are PayPal charging you in terms of fees to receive the money?  So I got $477.55. So I guess $23, $22, $45. $45. $22.45 out of 500. So it's 4.5% about 4.49%.  Well, I'll split the fees with you.

38:58 - Trevor Bradford (Brandvoice)
  So if you sell. Send me another payment request for 50% of whatever fees they charge you, and then I'll send that through, and then we'd both.  Okay, I appreciate that.

39:10 - Matthew Kerns (12kernsmatthew@gmail.com)
  Take a look at the pain a little bit. Yeah, thanks. Okay. 11.22. Okay.

39:34 - Trevor Bradford (Brandvoice)
  I just sent that new one.

39:36 - Matthew Kerns (12kernsmatthew@gmail.com)
  It's only 11.11 dollars, but I appreciate that. Fees are fees, they?

39:41 - Trevor Bradford (Brandvoice)
  And they all mount up over the course of the year. Yeah. It's not arrived yet. Okay. I mean, they'll charge.  Yeah. I mean, they'll charge. Fees on Fees, but, you know.

40:16 - Matthew Kerns (12kernsmatthew@gmail.com)
  There we go. Okay. All right. Thank you. Then I'll push it. Should be able to do it within a few minutes here.  Okay. Yeah. And then let me just, maybe I'll just do that right now. So it'll be there in lovable.
  ACTION ITEM: Send Trevor invoice/receipt for $500 PayPal payment - WATCH: https://fathom.video/share/EcdijzxNSsAkTbTN5hJPspJx2WPqho33?timestamp=2460.9999

40:57 - Trevor Bradford (Brandvoice)
  Okay. Okay. Yeah. Okay. Okay. Okay. Matt, when you get a minute, and you don't need to do this today, know you've got a busy day, but if you would send me through an invoice for the payments that I've made, just so that I can keep my accountant happy, that would be great.

41:25 - Matthew Kerns (12kernsmatthew@gmail.com)
  Okay, yeah, I will. Thanks. So the last, the first payment, I think it was through Payment Link, so I just want to make sure that you got an invoice for that one.

41:50 - Trevor Bradford (Brandvoice)
  Yeah, the first 500 for the first half of Phase 1, you sent me an invoice, I got that.

41:57 - Matthew Kerns (12kernsmatthew@gmail.com)
  Sounds good, okay. Okay.

42:09 - Trevor Bradford (Brandvoice)
  So the only thing is that it's gone to Infinity Vault, but don't worry, I'll sort that out at my end.

42:18 - Matthew Kerns (12kernsmatthew@gmail.com)
  Oh, right. Okay. Yep. Got this second business now. Okay. So merge domain. Okay. Now that's pushed. So it should be shared.  It's showing up and lovable. Yeah. I'm just going to confirm that, by the way, I don't know if you published last time, but I just want to make sure that we can get it published if that's what you want.  But I left that up to you so you can test locally and lovable first and then publish when you want.

43:25 - Trevor Bradford (Brandvoice)
  Test first, think. Yeah. Before we decide if we're going to publish or not. And then because I'm sure there might be a couple of questions that I have before it's ready to share.  Yeah.

43:42 - Matthew Kerns (12kernsmatthew@gmail.com)
  Fine.

43:42 - Trevor Bradford (Brandvoice)
  Where's my lovable tab come? I always have too many pages on that. Yeah.

43:56 - Matthew Kerns (12kernsmatthew@gmail.com)
  I'm not sure if there's a way to keep them at bay. been timearte. No.

44:04 - Trevor Bradford (Brandvoice)
  Right, so, close all the PayPal stuff, there we go, right at the back, of course it was, so I'll share, I'll just refresh the page.  Right, Matt, I'm going to share this page with you, if you just confirm that this is correct.

44:38 - Matthew Kerns (12kernsmatthew@gmail.com)
  Okay. Sharing screen, or? Yeah, sharing the screen.

44:44 - Trevor Bradford (Brandvoice)
  Okay. Okay, this is what I'm seeing now after refreshing.

44:51 - Matthew Kerns (12kernsmatthew@gmail.com)
  Yep.

44:52 - Trevor Bradford (Brandvoice)
  So that looks, that looks right. Now we've still got this stuff down here, where. We don't have any functionality, and I thought we were going to lose that page map.

45:04 - Matthew Kerns (12kernsmatthew@gmail.com)
  Okay, and this is the page that you land on, right? Yeah, because on the brand diagnostic, obviously that works.

45:13 - Trevor Bradford (Brandvoice)
  We've got our insight-driven page, but we don't have any functionality on distinctive or empathetic. Right. Other than some really thin training, and it's really not up to standard for either an app or a course.  It's just a bit of blurb. So, of course, what I'll do, I'll put together training videos on the idea framework as well, that at the appropriate time when the videos are completed and they're hosted wherever they end up, we can then put links in the app to the training.  But we'll do that when I've done the videos, and we finalize the app so that when I'm looking at the page, and I'm scripting  So capture and what's happening when I'm using the app, I can put that into training so that there's no doubt in the mind of the user what they should be doing and what the app will deliver.  But it's a chicken and egg thing. First, I have to have the app in order to do the screen capture to do the training.  So if you recall on this page, the diagnostic we know all about. You have to sign in for that.  OK, it remembers me. That's great. Tom says I'm signed in. OK. Insight. So this is this the latest. This is isn't it.  The interactive insight module. You change the text on this is all completely ready to go. We've got various things here.  It pushes to the pushes to the brand canvas, I assume.

46:56 - Matthew Kerns (12kernsmatthew@gmail.com)
  Yeah. So you're saying like when you hit complete frame. Yeah.

47:00 - Trevor Bradford (Brandvoice)
  Yeah, but I haven't put anything in yet. So what I think we should do, and we've got to start here, okay, on that place, we talk about the next steps, right?  So if I follow the route on the navigator bar, that page isn't there. Sorry, which page?

47:37 - Matthew Kerns (12kernsmatthew@gmail.com)
  Oh, the first page?

47:40 - Trevor Bradford (Brandvoice)
  Did something change there? Start here.

47:45 - Matthew Kerns (12kernsmatthew@gmail.com)
  I wonder if you click Idea Brand Coach if it goes to that first page. Yeah. Yeah.

47:51 - Trevor Bradford (Brandvoice)
  This is one of the things that we said early on, that because we didn't have any functionality, Yeah.

48:04 - Matthew Kerns (12kernsmatthew@gmail.com)
  So I guess I'm wondering what should we show instead, because I can add a redirect pretty easily to a different page if we want to completely scrap this page, but we could also just show the ones that work, so the insight modules there, right, and then all these things down below are there.  Yeah.

48:28 - Trevor Bradford (Brandvoice)
  You see, we've got some hangovers from the original design that I did in Lovable. For example, we're still talking about the Value Lens Generator, but up here we've got the Brand Copy Generator.  So this is why I need to be able to go through it and just note anything that is inconsistent so that we can change the text.  Or I can change the text if this is on Lovable. I just tell it to change the text, I suppose, don't I?  Yeah, I think so.

48:58 - Matthew Kerns (12kernsmatthew@gmail.com)
  And then I guess we can do that. And then if, if anything breaks, if you notice anything breaks and you can't fix it, or you don't want to try and fix it because it might break other things or something, then just let me know and I can, I can go in there.  Yeah.

49:13 - Trevor Bradford (Brandvoice)
  I won't want to mess with the functionality, Matt. What I want to do now is arrive at how it looks, the finished article for beta.  Yep. Make sure all the text makes sense, has got the right tone of voice, that kind of thing, and then give it to some people to play with.  In parallel with that, or not in parallel, but subsequent to that, I'll do the LinkedIn piece we talked about, and then, you know, we can talk about that when you get back and see, see how that works.  It might, it might be so simple. All you've got to do is just connect it to a database. I'm hoping that's the case, because it's all already built here.  Okay. Okay. And it's just a duplicate. What I want to do is make sure that all the text is right on this before I duplicate it so that we haven't got to do lots of parallel processing.  And so regarding this page, do you want me to have a think about it and come back to you?  Because I know you're pressed on time. You've got to go. What if I come back to you with some notes?  Now this is on lovable. I'll work my way through it and I'll do you one of my mood board flow things with with some notes that should make it as clear as possible what I'm talking about.  And we'll take it from there. I mean, if you recall, when we looked in the when I did the free form flow, this this page, we we actually.  I think we've been it. OK.

50:53 - Matthew Kerns (12kernsmatthew@gmail.com)
  Yeah. In fact, I'll just share with you.

50:58 - Trevor Bradford (Brandvoice)
  Yeah, was trying to pull up my free form.

51:00 - Matthew Kerns (12kernsmatthew@gmail.com)
  Now, but the app for some reason has given me a problem, so, but I do also have the recording from last time, could go back and watch that, or if you think it's quick, we can just do it here.

51:14 - Trevor Bradford (Brandvoice)
  Yeah, I'll show you, I'll just show you the board that I always refer to. Okay, yeah, that's good. I'll find it.  Idea Brand Co-Chapter, where's that gone? There we go, it wasn't in a tab, it's a separate tab. Right, so, this was it Matt.  Yeah. From way back when we talked about chopping the app down, you know, it used to be like this, body busy, various pages, this here's the page that we're talking about, and actually we said, all right, we're going to get rid of all of that, we're going to have a diagnostic, we're going to do a download, we've got a sign up page, which eventually will be a payment thing, and you've addressed the payment costs on that, it's not linked up to a payment, hey Trevor, can you hear me okay?  Yeah, got you.

52:40 - Matthew Kerns (12kernsmatthew@gmail.com)
  So my computer froze about 30 seconds ago, think, but I'd sell them for my phone, so.

52:47 - Trevor Bradford (Brandvoice)
  All right, I'll start over, so just to recap, this is what we looked like before, and I said, let's chop, let's chop a lot of this away, and most  Most of it is about this page here, which is the one that we're talking about, it's that one, there's the functionality on the first two modules, I said okay let's chop all of that, we're going to do the diagnostic, there's the page, and then we're into the app which starts with avatar, moves on to the insight module, moves on to the brand coach module, then the brand canvas strategy module, and then what was the value lens copy generator, and we've now called brand copy generator, so that was a simplified flow, so that page that we were looking at that's transferred over now to Liverpool, in this model at least is redundant.  Now do you feel that it ought to be redundant? Yeah. Yeah. Yeah. And we ought to have it there, and in which case we need to modify it, or is it surplus to requirements at the moment?

54:12 - Matthew Kerns (12kernsmatthew@gmail.com)
  So we could, so I think there's two options. We could remove the page, in which case we should have a default landing page, which might just be the avatar page.  Yeah.

54:25 - Trevor Bradford (Brandvoice)
  That's the first one.

54:26 - Matthew Kerns (12kernsmatthew@gmail.com)
  So they just jump right in, right? And then the other option would be, so even clicking that idea brand coach would direct to the avatar page.  So we could do that, and that would be click. The other option is, if you review the page, and you think, okay, we can have the initial, we can have the rest of the page, just adjust the copy, and maybe hide the DEA parts, because they're not fully functional.  Um, in the app, then I think that's another option.

55:03 - Trevor Bradford (Brandvoice)
  Okay. Well, I'll tell you what, let's leave the page there for the moment and I'll do a schematic that shows you what it, what it should be.  And then you can just make the minor adjustments to it rather than take it all out. I have to mess with coding and page directs and stuff like that.  Uh, and that's, I think that would probably be the easiest thing. And I'll just look at that page and treat it as a homepage.  And, um, I don't know, maybe we might want to put a video player on it or something like that.  Uh, but I'll have a think about that. And we can talk about that when, when we get, when you get back from your, your aunt's move.  Cause I know you've got to go. We're coming up on the hour and I know you've got a busy day.  Okay.

55:49 - Matthew Kerns (12kernsmatthew@gmail.com)
  Okay. Yeah. I appreciate that. Um, that sounds good to me.
  ACTION ITEM: Create new board w/ screenshots + notes; share w/ Matt; then duplicate diagnostic-only project - WATCH: https://fathom.video/share/EcdijzxNSsAkTbTN5hJPspJx2WPqho33?timestamp=3354.9999

55:56 - Trevor Bradford (Brandvoice)
  Yeah. think I'd, like to think about it for a bit. Anyway, before making decisions on it, because it still has some value and function.  So, yeah, so I may do a new board, I think, because this was all a bit busy. So now we've got a functioning app, pretty much.  Then I'll do screenshots of each of the pages and make any notes in a new project board. And then I'll share that with you.  Yeah, cool.

56:26 - Matthew Kerns (12kernsmatthew@gmail.com)
  Sounds good. And then I was wondering, I guess that's the next step, right? And then any, I'll try and get any fix ups done quickly so you can roll out soon.  And then you can start getting it tested. Great.

56:45 - Trevor Bradford (Brandvoice)
  OK, because if it goes on too much longer, people will be coming into the Christmas period and I won't get anybody having the time or interest to do it.  And then we'll be in January and we've lost a big chunk of time. Yep.

57:00 - Matthew Kerns (12kernsmatthew@gmail.com)
  So tonight, we're going to drive today, and then tonight, I might have another window of opportunity where I can be connected to Wi-Fi and code some stuff.  So if there's any updates that you think of and you can send over within the next, I guess, 12, 15 hours, then I can probably make some adjustments.  Okay, I'll get on to that then.

57:34 - Trevor Bradford (Brandvoice)
  Thank you again for all your help. I really appreciate it. I hope things go well with your aunt, and we'll speak soon.  All right.

57:42 - Matthew Kerns (12kernsmatthew@gmail.com)
  Thank you. Yeah, we just packed up the 26-foot truck yesterday, so it's all built to the brim. So we got to now drive it down and then move it.  But yeah, thank you. Sounds good. We'll talk soon then. Excellent.

57:57 - Trevor Bradford (Brandvoice)
  Okay. Have a good trip.

57:58 - Matthew Kerns (12kernsmatthew@gmail.com)
  Thank you. All right. See you.

## Action Items

-

## Next Steps

-
