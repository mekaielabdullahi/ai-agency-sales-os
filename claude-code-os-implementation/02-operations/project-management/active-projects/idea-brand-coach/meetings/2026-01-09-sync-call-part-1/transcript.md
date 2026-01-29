# Sync Call Part 1 - January 9, 2026

## Transcript

Trevor. This meeting is being recorded. Hi, Matt. Good to see you. Did you have a good Christmas?

Matthew Kerns
Good to see you. Yeah, it was awesome.

Trevor Bradford
What did you do?

Matthew Kerns
It was just very, very relaxed. I have a small family, so it's just me and my parents. And, yeah, we just kind of spent some time together.

I spent like two days with them, just like eight hours each day about. So that was really nice. Got some good family time in.

Trevor Bradford
How was yours? Oh, it was fantastic. On Christmas Day, we flew out to Mexico, and we had almost 10 days there, and that was fantastic.

We did quite a bit of outdoor stuff. We were on a sort of an adventure boat trip thing, where there was snorkeling and kayaking and a bit of hiking and other stuff in the sea of course.

Cortez, you know, which is in the bottom end of, well, it's on the west side of America. You know how California goes down in that long, thin strip that turns into Mexico?

Well, it was that bay area there.

Matthew Kerns
And it was just amazing. Cool. Like right next to Baja, California.

Trevor Bradford
Exactly. That's exactly where it is.

Matthew Kerns
Wow. Sweet. Yeah, that's amazing. I love, my family used to take us on vacations to Mexico. So that's why I love the Titan Cancun trip.

And then like, but yeah, going to Mexico is super fond memories. So getting to do that every time, that's so cool that you got to do that over Christmas.

Trevor Bradford
Yeah, it was. It was great. The only downside was that we were on this boat and even telephone signals weren't that great.

And the Wi-Fi was so slow as to being virtually non-existent. So I wasn't really able to do much in terms of work.

I reviewing the app while I was awake. And yesterday was my first full day at work. So I've been working through, you know, a pile of stuff that needed immediate action.

ACTION ITEM
Deep-dive app/code review; send feedback to Matt
So I spent sort of 20 minutes or so just looking at where we are. But I think it will probably be best, Matt, if you walk me through what you've done since our last meeting, I know that there were Fathom notes and all that kind of thing that we talked about.

And then some subsequent comments in WeChat, WhatsApp, rather. So if you want to just take me through the state of play, and then what I'll do once we've done that is I'll get deeply into it over the weekend.

Matthew Kerns
Okay, sounds good. Yeah, so I, to be honest, I didn't spend too much time preparing for this call. saying?

Tom. Hey Thank

Trevor Bradford
That sounds good. We'll wing it.

Matthew Kerns
Yeah, sounds good. Okay. I'm just going to request a share screen. So, yeah, I think I'll probably just go through the recent WhatsApp because I think I summarized things in there and then that'll get my brain going and then we can dive in to where we're at.

Yeah, I want to figure out, like, what do we need to get it in front of beta testers? I think that's the objective.

Trevor Bradford
Yeah.

Matthew Kerns
And, like, what quality bar do we want for that as well? But, okay.

Trevor Bradford
So I think where we left it, if I recall, was that we were talking about the knowledge base that the app draws from.

SCREEN SHARING
Matthew started screen sharing
And I think you updated that, didn't you? And you tested it with Claude. Yeah. you delivered better outcomes.

Matthew Kerns
Yeah, exactly. Yeah. I remember now the brand name, like pulling the brand name from all the context was took longer than I expected because I was like, shouldn't it be obvious what the brand name is?

I don't know, but that one took a little while. But I think it, it, so the last time that I tested it, it was working for just getting the brand name on the document.

The other context, you know, I worked through some things and it, it was doing decently well, but I'm sure that there's some things that when you test it, you'll notice like, oh, it didn't do this that well, or it didn't do that, that well.

So I definitely want your feedback on the, because the document generation is the key thing that beta testers will want to pull out of using the app.

Uh, right.

Trevor Bradford
Yeah.

Matthew Kerns
So, yeah. So any like refinements, just any feedback at all that you have, just shoot it right over as soon as you know what it is, uh, and I'll work on getting it.

Trevor Bradford
I I did do a fresh output of the last set of stuff from Brand Coach and the formatting of the PDF looks much better.

Matthew Kerns
Okay. Yeah. Yeah. I tried to update that. I'm glad it looks better for you.

Trevor Bradford
I mean, it doesn't have idea of branding on it or anything like that. But as I said at the time, I think that was less of a concern for me in the short term, rather than the fact that it's a presentable document that's come out of the app.

Matthew Kerns
Yeah. I guess like for now, if it's usable, if it has usable content, that's a higher priority than making it super professional and presentable.

Trevor Bradford
Right. Yeah.

Matthew Kerns
Okay. Um, okay. Okay. Let me see if I can read through some of this stuff. So... So this stuff we talked about, so there's that knowledge base, I haven't hooked up that yet, so that this Google Drive folder is not yet hooked up with the knowledge base, so that you can upload that, but we can figure out how to prioritize that if we want to.

So let me just go through my recent updates. Yeah, okay, this is a good place to start. So I got the interactive insights fields mapped properly now.

So that context should show up in the chat messages and brand strategy document export. So the interactive insights is one of the tabs at the top, and that should be all connected now to the document export as well as the chat.

Trevor Bradford
Okay. Is that pulling from the avatar, as well?

Matthew Kerns
The, you're talking about this, the export and the chats?

Trevor Bradford
No, the interactive insight module, you know, we've got things like buyer intent and buyer motivation, emotional triggers, and shopper type, and all of those things come from the avatar 2.0 tool.

So what we don't want to do, obviously, is replicate what's happening in the avatar 2.0 tool.

Matthew Kerns
Yeah, that's something that we talked about, I think we want to not duplicate that stuff, right, like there's buyer intent here, then there's buyer intent here.

So I think that might be like a, so we, we can test right now, if you want, we can test if it pulls from avatar 2.0.

ACTION ITEM
Fix Interactive Insights UI: truncate/scroll + accept/reject; then wire Avatar 2.0 + dynamic prompts
So I think. Yeah. It might. I'm not sure with these AI suggestions. Let's just test it. I'm not sure.

I don't think I hooked that part up yet. Yeah, see, this still is doing the instruction AI suggestions.

Trevor Bradford
Yeah.

Matthew Kerns
That's something we're going to want to update, right? Get it to actually update this with the same experience that the canvas has.

Do you remember what we did to the canvas where it has the accept or reject?

Trevor Bradford
Yes, that's right.

Matthew Kerns
So I'm not sure if you've seen this yet, actually, but there's this AI suggestion, current content. Looks like that's actually cut off there.

I can't even see it, and I can't scroll through it. So that's something that I can fix. Then suggested replacement.

So then it comes out with this, beacon of light and stronghold of security for TCG enthusiasts by providing top quality protection solutions that safeguard their cherished card collections.

We empower collectors to confidently showcase their cards and compete in tournaments, ensuring that they're always battle ready while preserving the value and integrity of their investments.

So I know that this pulls from, I think I mentioned battle ready in the chat and then preserving their investments, I think is something from one of these other sections.

So I think it does that well. Actually, if you look at this, the, so the previous one I had generated with this AI suggestion thing, and it's the exact same thing.

Trevor Bradford
I think. Oh, I see. Okay. So it's just, can you do the same thing over?

Matthew Kerns
Yeah. I'm a bit confused by that because I would think that it would do something at least a tiny bit different because LMs are supposed to be non-deterministic, but it looks like it's exactly word for word, as can tell.

But anyways, so we can accept or reject and then there's this little notification down here, your original content has been preserved, suggestion dismissed.

That's cool, but we can bring that, we need to bring that to this interactive insights module.

Trevor Bradford
I mean, for me, Matt, the most important thing is that each step of the process is logical that the user goes through.

And it's important that the next step that they complete, if it requires information from the previous step, such as Avatar 2.0, was obviously shouldn't but

It all pulls through, so they haven't got to do multiple inputs and start over or figure too much out for themselves, because the whole value of this to them is that it takes so much of the work away and gives them something far better than they would have arrived at themselves anyway.

Matthew Kerns
Yeah, okay, so let's just test that connection really quick. So what I think, I think it should be connected, because I think the way that the way that it's supposed to work is this should get saved to the Supabase database, and then that there's like a hybrid saving model that generates embeddings and stores that the semantic meaning of this text in a vector storage for the LLM.

Okay. And then each of these should be pulling from that as well. Okay. From where it's stored. So there's a chance that it's not yet, but I just want to test it out real quick.

So, but how would I, how would I test this? Because we have, say, avatar name. So the thing is, the AI, I might not be able to test this yet, because the get AI suggestions only creates instructions, it doesn't create content, right?

Trevor Bradford
Right. Okay. Well, if you scroll to the top of the page on that one, as you can see, those four or five buttons there are the five, no, no, a little bit further down.

We lost it at the moment. Yeah. There we go. Framework. Yeah. Those are the four stroke five parts of the avatar diagram.

Do you remember that I showed you from the book? Yeah. And they correspond to a worksheet before I had the app here.

But the user would use ChatGPT or their own information to fill in each of those sections. Now, of course, obviously what we're doing now is we're helping them with AI and anything else that they've inputted into the avatar.

Matthew Kerns
Yeah.

Trevor Bradford
So this is the bit that's always confused me about this particular module, the Insight module, is that it seems to duplicate or replicate Avatar 2.0.

Matthew Kerns
I think, actually, it's sort of like this is your initial builder. Yeah. I might adjust this and say, instead of detailed here, I might frame it as, like, this is your initial builder.

You have buying behavior. You kind of, like, you pick this, right? You pick at a high level. And then Interactive Insight is where you dive deeper.

And you So this one, maybe the copy should be like, this is where we want you to think deeply about this section.

We know that you've selected, what was it, considering options for buyer intent. Like, if we assume there's one avatar for now, just to keep it simple, we can surface that here as part of the copy and say, and prompt them and say like, okay, for someone, for your target customer who's considering options, and then for that, like have a prompt right here that's sort of dynamically generated from that previous page, that would tie them together.

And then they can dive deeper in this part.

Trevor Bradford
Okay. Yeah. And once we're clear about how that works, and when it does work, then if necessary, I can just do a quick

It's a instructional video that talks, which I'd always intended to do anyway, that takes people through each of the modules and tools, culminating in the output of the strategy document.

So, you know, if it needs clarification, you know, with a video link or anything like that, then, you know, it's easy to do.

Matthew Kerns
Yeah. Do you, by any chance, have, do you pay for Loom?

Trevor Bradford
No, I use the free version at the moment.

Matthew Kerns
Okay. I'm not sure if it's available on the free version, but there's like a, there's a SOP generator with Loom.

I think it's the, it might be the paid version though. So if you record something with Loom, it'll create like a document as well, like as you're recording.

So that could be useful, but we could also generate it later another way. It's just like more efficient if it's, but I wouldn't say it's completely necessary.

Trevor Bradford
No. So is that to generate an SOP on how to use the app? Is that the intent?

Matthew Kerns
Yeah, that's what I'm thinking. Like, if we can provide a video and also a document, that might be helpful for people.

Trevor Bradford
Right, okay. Well, the video that I was thinking of doing was the AI version, where, you know, super quick for me now, I can just type in what I want to say.

The avatar says it, whereas with Loom, I'd have to record each one.

Matthew Kerns
Right.

Trevor Bradford
So I'd like to avoid that if I can, for consistency's sake, as well as just time and repeated takes and edits and things like that when you're recording live.

It's a bit of a pain. And that's the whole benefit of using the avatar.

Matthew Kerns
Yeah, for sure. Whatever works. Um, I think if we just have a video output, that's, that's going to be...

be awesome. Video kind of like walkthrough would be cool. But for beta, for the beta stage, it doesn't have to be perfect, but it's good if we think about what the ideal would be.

But ultimately, I want to have a full like onboarding, click through experience, but that's probably not for beta. So I want to say focus on the beta as much as possible.

So yeah, I think if you do, yeah, if you once you generate a video, like we can, I mean, with the tool with AI tools available now, we can generate a document from whatever video you make pretty quickly.

So, but let's figure out this part, this, get AI help and get AI suggestions. I think we need to probably pick one.

Right?

Trevor Bradford
Yeah. I think get AI help is a better option. So if you're filling out this as the user, would you, as the user, Matt, because you've got your brand and you've been doing your own inputs into testing at your end, would you expect that having put some stuff into your avatar element of the process, avatar tool, that the insight tool would prompt you for more input in the way that it's doing at the moment, or that it would help you generate input?

Or is that a sequential thing? It tells you what you need to do and then will offer you suggestions if you're struggling.

It's a little bit like ChatGPT works.

Matthew Kerns
You've got to give it something to work with. the view stomach.

Trevor Bradford
But once you have, it then offers you options. Would you like me to do this? What about that? You know, that kind of thing.

Just let me know what you want to do. You obviously worked with it 1000 times by now, like me.

And I'm thinking, you know, whatever we do ought to be and ought to feel comfortable for people. Because by now, everybody who is in our space is used to using chat GPT or Claude or similar.

And they always come back with an iterative response at the end of every thing that it gives you. It says, what would you want to do now?

Would you like this? Would you like that? Just let me know which way you want to go. And so that's that two level thing that I was referring to.

Obviously, you put something in and then it looks at it and offers to build on it. And

Matthew Kerns
Exactly. Yeah. So the way it is right now, what I was about to show you is my natural instinct is to basically, here's the preview.

Okay. My natural instinct would be to take this suggestion and I want to use an LLM. So I want to take this and I want to say, Hey, I'm working on infinity vaults, help me do this.

And just copy and paste it into my chat GPT and then see what it says. Cause I want to leverage it to move quickly as possible.

Right? So this thing is going to create for me answers. And then I'm just like, before it even finishes, I'm going to say, okay, give me a, a descriptive detailed.

Summary of the buyer intent to send to my brand coach. Right. And then whenever it's done, it's not even done typing yet, but then it'll create that for me.

So what I'm thinking for your website is for your app is it would be like, I really want to pull this brand coach out so it's not trapped behind here.

Cause right now it's like, I gotta, I gotta copy and paste things. I gotta go back to here. gotta find which conversation I have, I have with it, which is, it's good to be able to look this stuff up and have the history.

But what I want, what I really want is a little helper right here that I can just click and instead of all these buttons, I just have a widget right here.

That's like, you know, like I just click it and it knows I'm working on the buyer intent and it's like, you know, it's giving me.

And then I'm able to, like, learn about, I'm able to watch the content, and then I'm able to engage with this widget on the side here.

So that's, again, that's more probably future vision and, like, a feature we would need to build. But what I would want is for it to help me, like, to generate things for me, like, use the power of AI, where I just put in, I put in a little bit, like, the key is, like, leverage, right?

Like, I put in a little bit, I put in what I'm thinking, because we need to drive these LLMs at the end of the day, like, they can't do it all by themselves yet.

No. So, but, like, if I just put in a little bit of input, I want an amazing output right here.

And I want the magic of, like, I'm using Trevor's app, and it's creating for me, like, this amazing buyer.

So that's what I want as a user at the end of the day. And if it's a widget, that's cool, but for now, it can definitely be a button right here.

Trevor Bradford
Okay. Well, the logic is the same. I get that. The widget idea is super, because it seems such a user-friendly way to approach it.

Matthew Kerns
Yeah, I agree. And then it can also tie into, like, long-term. Like, you already have your Eleven Labs HeyGen personal-branded avatar, AI avatar built out.

We can make it into, like, you know, if you want, like, this is Trevor, your coach in the corner here.

Like, we can think about that later, but that would be more longer-term. But I think that personal branding is going to be huge, a good position to be in.

then… Yeah. You a good personal brand, which you already have been developing, and so if we can just bring it forward in the website, it might be a good option.

It might take time, so we can figure that out, but yeah, we can talk more about that later. So, for now, I think I can, to simplify, I can work on removing, well, so get AI help or get AI suggestions.

I'm almost thinking, is there another way we can say this, where it's like, AI enhance, and then, like, whatever.

So type here, it'll enhance it. But I like the idea of helper suggestions, and then we can hit approve or reject from whatever it suggests, right?

Yeah. Because we don't want it to just automatically do that. So, OK, I'll stick with AI help, and then I'll just bring the other one over, that same experience as accept or reject.

Should we quickly go through the Canvas generation thing?

Trevor Bradford
Yeah.

Matthew Kerns
OK, so I think I fixed up PDF as well. Let me go back to the WhatsApp while it's generating.

It does take a little bit of time.

Trevor Bradford
The output of the PDF is nice and clean, and it looks more than acceptable, I think.

Matthew Kerns
Cool.

Trevor Bradford
So what I didn't do is update any of, on my end, any of the inputs. So it was working with what I'd input.

So some of it wasn't particularly specific. It was quite generic in terms of the information that it had provided.

But that was before I think you'd hooked it up to the knowledge base and improved that. So what I hadn't done was go through it all again, start a brand new chat or a new project inside the app, and then test it all from scratch, which is what I think I need to do.

So all I was doing was just testing the quality of the output and to see if what came out looked like something you would expect out of the brand module.

My only observation, I think, though, Matt, is that the headings are in blue, and we don't have that sort of fairly mid-blue.

There's a color palette inside the app. It's all black or white, primarily with one or two colored highlights. So it seems a little bit off brand from a design point of view.

But hey, I'm not looking to reinvent the wheel here. Certainly from the point of view of the app, it will be fine.

But I just wonder whether we should just have it all black, rather than have colored headings. If that's a quick fix.

Matthew Kerns
Yeah, I don't think it will take much time. Well, yellow is a bit, I might need to add some borders to make the yellow actually not blend in with the white background.

But either way, think it'll be quick. Just whatever, I think whatever you want, ideally, like if you just tell me that, then I can, I can the gold one.

Trevor Bradford
Oh, okay. Okay. Yeah, let's not worry about it in the short term, I think. It's just something to have on our list for final fixes.

But for getting it to beta, really what we want to do is as quickly as we can get to a point where this works the way that we envisage it.

ACTION ITEM
Decide Journey page for beta; if kept, add placeholder text
It started the process. you start with your interactive start here quiz, know, the diagnostic. And that gets you into the whole thing.

And it's consistent all the way through. As I say, my big question is on that journey page, whether we should even have that landing page because so little of it.

see. That has got functionality when you click through to the modules, so the diagnostic works, the insight section is active, but the second two, the distinctive and empathetic, or three, rather, and authentic, they're just, there's no functionality there, really, to speak of.

So, we talked about making those things more functional at a phase two. So for the phase one, I'm wondering, from a user point of view, do they have a role?

And I'm very close to this, so I'm sort of asking you as a user, if you run through this, do they add to your experience, or are they just confusing?

Matthew Kerns
I think, I know we're about to run out of time here, so I have to jump back on, but I think it could be cool to to So, thank you much.

Thank you much. welcome. So. you're welcome. you much. I'm here

**Recording:** https://fathom.video/share/eFMC8aNnU3TuSk8dVTNCRovmjLPJRtxe
