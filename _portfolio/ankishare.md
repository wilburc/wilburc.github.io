---
layout: writeup
title: AnkiShare
intro: Providing reliable study material for medical students.
details: UX Design
---

- Capstone Project in Informatics at U.C. Irvine
- 9-month duration
- I was responsible for design, in our group of 5.

### Background

Our client, a student in medical school, wanted a way for students to easily share the <i>best</i> <a href='http://ankisrs.net'>Anki</a> flash cards. At the time, students had to personally ask other students to send them their decks. Current issues they faced:

- Deck availability/variety limited to who you knew
- Awkward to ask peers for their study materials
- Must be sent manually through IM/email

While the final product would be up to us to design, our client presented us with his vision.

> “Imagine a collaborative app that has everyone’s flashcards, and it has an algorithm that magically picks out the ‘best’ cards for any given category, curating them into ‘master decks’.”

We mindlessly nodded in agreement, not even giving the term “magically” a second thought. A happy client makes a happy professor, which results in good grades and makes happy students. 

### Research & Requirements

Thankfully, we knew to start with research. Looking back, the research helped us immensely in getting out of the circles that we were walking in, not knowing how to make decisions.

#### Surveys
We were given access to the medical students mailing list, and sent out several surveys throughout the duration of the project. We used surveys to learn about general habits and trends throughout the student body, both validating and challenging our ideas.

- All students use Anki cards
- Most (90%+) students shared cards with their peers
- They spend <i>a lot</i> of time studying. 

#### Contextual Inquiry 

We also were able to meet with some students, and watch them study (sort of). They walked us through their file libraries, and talked about their study habits and flashcard preferences. 

- Most students had thousands of cards in their libraries
- Everyone categorized/labelled their decks differently
- Similarly, everyone’s cards were in different formats (Question on front/answer in back, picture on front/descriptions on back, etc.)

Additionally, we began using Anki software ourselves, to learn about the application and how it works.

#### Personas
With all this information and interaction with the users, we identifed two personas that these students almost all fell into: the downloader, and the uploader. 

![ankishare personas](/files/ankishare_personas.png "AnkiShare Personas")

### Design
 
While we were conducting our research, we also began sketching ideas for what this product was to be. In an effort to please our client, we worked off of his initial vision:

- Repository of cards
- “Best cards” algorithm


Repository of cards was fairly simple and straightforward — they can upload their decks. But ”best cards?” What does that mean, and how could we write an <i>algorithm</i> to figure that out?

#### “Best Card”
 At the beginning of the project, we had identified that the technical skill amongst our team was not very strong at all. Yet, we still entertained ideas regarding image-recognition, machine learning, and basically creating a supercomputer. This was a costly mistake on our part; we spent <i>months</i> trying to figure out what we could do to identify the “best cards”

At this point, our research had shown that some people’s cards didn’t even use text; just figures from the textbook, or screenshots of their professor’s slides. You can’t just <i>parse</i> an image (well maybe you can, but we didn’t know how). This helped nudge us towards the idea that we’d have to use <i>people</i> to help us; we’d essentially have to crowdsource. 

I looked to real-world products that do the same thing. Communities where the audience decides what deserves to be seen. <a href='http://reddit.com'>Reddit</a>’s upvote/downvote system was one that we thought about, along with a star-based rating system a la <a href='http://yelp.com'>Yelp</a>. 

![ankishare bestcard](/files/ankishare_bestcard.png "AnkiShare Best Card")

We began to question if this was the right choice: we want to alleviate all their pain-points in getting cards, so they can spend more time doing the actual studying. With this in mind, would crowdsourcing, having them spend more time with our product and less time studying, be the solution?	

Almost as a compromise, I suggested simply tracking the # of hits a deck gets, as a proxy for its popularity, and by extension, quality. While bbviously not as accurate as other methods, but I felt that it was a decision that needed to be made.

#### Repository Structure
During that ordeal, we were also thinking of ways to structure our deck “repository.” Our research showed that students would generally know what decks they were looking for, whether it be “material for Professor X’s anatomy final,” or “Histology 101, Week 3.” This translated into us needing an intuitive, precise, structure that could let students really lock-in on what they had in mind.

After looking at many existing decks created by students, we noticed that there were many ways they were classified — some people made decks by course, some by topic, etc. . This suggested several possible “directory structures,” such as 

- Topic (Anatomy) > Sub-topic (Hands) > Professor (Jones) > Lecture (Week 2)
- Student Year (MS1) > Quarter (Winter 2013) > Course (Anatomy 101) > Lecture (Week 2)
- Course (Anatomy 101) > Topic (Hands) > Sub-topic (Thumbs?)

We originally wanted decks to be clearly separated into “folders” to easily create the “master decks” for each category (its given folder). However, now that we weren’t doing master decks, they didn’t need to be in folders. Therefore, we decided to not separate them at all, and instead implement a filter. 

By identifying all distinctive properties of these decks (professor, topic, lecture, etc.), we could figure out what filter fields to include. Unfortunately, this resulted in a cluttered filter, due to the massive number of courses, topics, and professors across the 4-year program. I had a theory that students only needed material for their given year, so we asked in a survey, and started asking our users during testing as well. Luckily, they confirmed that suspicion unanimously, and we were able to reduce 75% of the filter content by only showing options relevant to their given year.

![ankishare filter](/files/ankishare_filter.png "AnkiShare Filter")

### Core Functionality
We were able to narrow down the product to a simple DropBox-esque web application, that allowed the upload and download of files. 

### User Testing
To validate our product, test its usability, and receive feedback, we scheduled several rounds of user testing with medical students. 

Going in, I prepared a list of questions and tasks for students to complete. We defined success based on how quickly and easily they could perform these tasks. Watching even the most confident students struggle with the simplest of tasks was definitely a reality check for us. In addition to issues with the interface and layout, we were able to identify confusing copy, and incorrect assumptions. 

- “Is ‘author’ the author of the textbook the material is from, or the student who made the cards?”
- The filtered results appeared below the fold, much to the confusion of many students, who didn’t notice.
- Students tried creating accounts on the log-in page, and vice-versa.


Fortunately, the high-level concept of our product (“It’s basically a DropBox for Anki decks”) was easily understood and clear. To address the usability issues, we increased/decreased emphasis on certain call-to-actions, and cleaned up our copy.

#### Viewing & Editing
While students could easily download the deck that we specified, many expressed concerns for knowing which deck to download. They elaborated that when looking for decks, they want to know what they’re getting. Card format and “style” were much more important to them than we expected. Because of this, we quickly threw together a Preview feature that allowed them to view the decks in their entirety. With this new functionality, we decided to extend it to viewing <i>and</i> editing, to have students collaboratively curate these “best decks” manually. 


### Final Product
The final product was infinitely simpler than we could have ever expected, but effectively carried out its twin core functionalities: upload and download. 

![ankishare upload](/files/ankishare_upload.png "Final Upload Form")

![ankishare download](/files/ankishare_download.png "Final filter/download interface")

### What we learned

#### Design with real data/content
If we hadn’t seen the wide variety of deck formats, we would have likely assumed that flashcards were all Question Text/Answer Text. Luckily, we had plenty of access to real users and their files, and could make the system flexible. This also helped lead us to the “preview deck” functionality, knowing that students cared about what sort of format these decks were in before downloading. 

#### Tie back to the goal
We had some pretty interesting and ambitious ideas. The long duration of this project only made us lose focus even more, spending time on unnecessary and possibly detrimental functionality. By tying everything back to the main goal of sharing flash-cards, we were able to severely narrow down our scope and focus on our two core functions.

#### Test early and often
Several rounds of usability testing, along with surveys, allowed us to constantly validate our ideas and product, while also exposing weaknesses in AnkiShare’s usability. 

### Future Plans

#### Visual Design
It’s probably clear at this point that we had little to no time working on the visual design of this product. While I recognize the importance of an aesthetically pleasing product, I don’t hesitate to deliver something visually “acceptable” that works, given a deadline. Regardless, certain elements such as the typography, spacing, and color could be optimized.

#### Scalability
While intended for and limited to medical-school students, flashcards are used by all sorts of people in many different fields. The main concept of AnkiShare is in no way restricted to medicine, and AnkiShare could potentially be expanded and scaled to help other non-medical students as well. 

### Credits
Many thanks to AnkiShare team: Jazmynn Daos, Dillon Gee, Vamsi Koduru, and Kyla Lamontagne. 

### Thanks for reading!





















