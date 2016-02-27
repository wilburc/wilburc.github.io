---
layout: writeup
title: AnkiShare
intro: Providing reliable study material for medical students.
details: Product Design/UX Research
---

- Capstone Project in Informatics at U.C. Irvine, 9 months
- I was responsible for the research, mockups, and user-testing

## Background

*This is a story on translating research into requirements, product definition, and narrowing down complexity.*

Our client, a student in medical school, wanted an application that allowed students to easily share their <a href='http://ankisrs.net'>Anki</a> flash cards. His vision was: 

> This app connects everyone’s Anki accounts, pooling all their cards in its database. Students can access this database and all its files. Additionally, app has algorithms that can identify the _best_ cards for any given category, consolidating them into ‘master decks.’

He also described some pain-points he was trying to address:

- Annoying and tedious to send flashcards (the logistics)
- Deck availability limited to who you knew (especially relevant to incoming students)
- Awkward to ask your peers for their cards

## Research & Requirements

We started with research, which involved getting to know both the **users*** and the **Anki software** that we would be building for, to better understand their pain-points and context.

**Our client specified that this application would be limited to students of the U.C. Irvine School of Medicine.*

### Anki Software
As we had never used Anki software before, we downloaded the Anki desktop/mobile applications, and found some decks to play around with. 

- Anki software included on every incoming student’s iPad 
- Anki decks must be added to a user’s library from the *desktop* app, and are synced to devices from there (similar to putting songs on your iPod via iTunes back in the day)
- There is a built-in learning algorithm (hence its popularity with students, as we later confirmed)
- Code for the desktop-app *not* open-source

### Surveys
Access to all 400+ med-students was available through their school’s mailing list. 
We sent out surveys to validate our assumptions and mission.

- All students use Anki cards
- Most (90%+) students share cards with their peers\*, and aren’t picky about who they share with
- Students spend *a lot* of time studying
- Students study on their laptops and iPads

**This was important to us, as a common argument was “isn’t most of the value in the making of the cards?”*

### Contextual Inquiry 
These surveys also helped us meet with some students. They walked us through their file libraries and talked about their study habits and flashcard preferences. 

- Most students had 1,000–20,000 cards in their libraries
- Everyone categorized/labelled their decks differently
- Similarly, everyone’s cards were in different formats*
- The UC Irvine School of Medicine has a set curriculum — all students of any given year take the same courses

**We generally think of flashcards as question text on the front, answer text on the back. This was not the case at all. Many consisted of only screenshots, drawings, or just a few words.*

### Personas
With this information and interaction with the users, we identified two personas that these students almost all fell into: the **downloader**, and the **uploader**. 

<img src="/files/ankishare_personas.png" data-action="zoom">


This translated into two *key functionalities*: **uploading** and **downloading**.

### Research Summary 

- The **value** of the product lies in two main areas:
  1. Saves time spent communicating between students and sending decks
  2. Makes a *vast* wealth of resources available
- The **user’s environment** is a combination of iPad and laptop — decks have to be imported via the desktop app, so AnkiShare will be a web-application.
- **Anki Decks** are numerous and diverse in both content and format

## Design
 These values mostly\* aligned with our client’s original vision and its features:

- **Repository of cards** was a pretty simple concept to us — basically just a huge dump of cards that was nicely categorized.
- **Best Cards Algorithm** was something else, and the greatest design challenge we faced.

**While we did mention the “best card” algorithm to students, none expressed a strong interest in it. However, in an effort to please our client, we went with it anyway.*

### “Best Card”
 At the beginning of the project, we had identified that the technical skill amongst our team was not very strong. However, we were still naīve (“optimistic”) enough to entertain ideas regarding techniques such as image-recognition and machine learning.

Our client suggested grouping all similar/redundant cards together, and figuring out how to identify the best card for each group, aggregating all of *these* cards into the so-called “master deck.” 

- ALL CARDS
	- Anatomy 101 cards
		- Cards about the number of bones in the hand
			- *Best* card about number of bones in the hand

This *best* card would then be put into a *master* Anatomy 101 deck with all the other *best* cards.

Our research showed that this would be impossible — cards were in various formats, half of them not including any text. Content was the same, but not the formatting. It would be like comparing apples to apple pie — you can’t.

We weren’t going to give up that easily, though. While no algorithm could rank these cards, *people* could — our *users* could. 

I looked to real products that also promote content based on popularity among their users. <a href='http://reddit.com'>Reddit</a>’s upvote/downvote system was one that we thought about, along with <a href='http://yelp.com'>Yelp</a>’s star-based rating system.

<img src="/files/ankishare_bestcard.png" data-action="zoom">

The mockup above represents just one of *many* ideas we considered, imagining every possible way this could be achieved. 

I started to question whether or not this was even something we should have considered. Referring back to our initial goals and requirements, the value did *not* actually lie in this functionality. **We wanted to *save* students time, not have them spend *more* time rating cards**. 

However, this was met with some resistance both within the team and from the client. This functionality was important to them, in the supposed extra value it presented. Additionally, a fancy algorithm would boost the “cool-factor” of AnkiShare — which some considered to be important.

As a compromise, I suggested tracking the number of times a deck is downloaded, and displaying this value. This would act as a proxy for a deck’s popularity, and by extension, quality. While obviously a far cry from optimizing at the card level, I knew we had to get ourselves out of this hole we spent the last 3 months digging.

## Repository Structure

Our research showed that students would generally know what decks they were looking for, whether it be “material for Professor Wu’s Anatomy final,” or “Histology 101, Week 3.” This meant we needed an intuitive, precise, structure that could let students **easily pinpoint what they had in mind**.

However, upon looking at many of their existing decks, we noticed that there were many ways they were classified — some people made decks by course, some by topic, some by exam. There was no *one way* to create a directory structure:

<img src="/files/ankishare_hierarchy_example.png" data-action="zoom">

We instead decided to *not categorize them at all*, and implement a filter that runs across the entire library.

<img src="/files/ankishare_filter.png" data-action="zoom">

## Key Functionality
We were finally able to narrow down the product to a simple Dropbox-esque web application, that allowed students to perform our previously-defined key functionalities: **upload** and **download**.

## User Testing
To validate our product, test its usability, and receive feedback, we scheduled several rounds of user testing with medical students. 

Going in, I prepared a list of questions and tasks for students to complete. **We defined success based on how quickly and easily they could perform these tasks**. Watching even the most confident and tech-savvy students struggle with the simplest of tasks was definitely a reality check for us.

- **Ambiguous terminology in our copy**. For example, students didn’t know if “author” referred to the student who made the deck or the professor who wrote the textbook that the cards are based off of. We started including this in our surveys, to decide on which nomenclature to use.
- **The interface was confusing** to some. The most eye-opening to me was when we had a case of a <a href='https://www.nngroup.com/articles/illusion-of-completeness/'>false floor</a>. The student selected her filter fields, and the content appeared below the fold. They thought it never loaded, and gave me a “your thing is broken” look.
- **Clutter on the filter** was brought up many times, and hindered our testers’ ability to quickly locate a given deck — especially since many course names were similar.

Fortunately, the high-level concept of our product (“It’s basically a Dropbox for Anki decks”) was easily understood and clear. Students realized the value and basic workflow/functionality of the product. 

## Iteration 
Upon analysis of my notes from testing, I wrote my recommendations and the team implemented them.

### Auto-filter vs. Filter Button
To fix the issue with the false-floor, we implemented a “Filter” action button, instead of an auto-filter that loaded the content automatically, without re-loading the page. The page load would better indicate that the filter had been applied. We also fixed the responsive-ness of the application and slightly modified the sizing of some elements.

### Sorting by Student Year
Fixing the wall of text on the filter was a top priority for us — testing showed that this was the primary way students would locate decks. At the time, we were listing every single course the school offers under the “course” filter. I hypothesized that students would only be looking for courses corresponding to their given year, and after surveys, was proven correct. We modified the filter to only show the courses of the user’s year, **reducing 75% of the clutter**.

### Viewing & Editing
While students could easily download the deck that we specified, many expressed concerns for knowing which deck to download. They elaborated that when looking for decks, they want to know what they’re getting. **Card format and “style” were much more important to them than we expected.** Because of this, we quickly threw together a “Deck Preview” feature that allowed them to view the decks in their entirety before downloading. The plug-in we used also afforded us easy implementation of an “edit” function, promoting collaboration among the students in improving these decks.

## Final Product
The final product was infinitely simpler than we could have ever expected, but effectively carried out its two key functionalities: **upload** and **download**. 

<img src="/files/ankishare_upload.png" data-action="zoom">

<img src="/files/ankishare_download.png" data-action="zoom">

## What we learned

### Design with real data/content
If we hadn’t seen the wide variety of deck formats, we would have likely assumed that flashcards were all Question Text/Answer Text. Luckily, we had plenty of access to real users and their files, and could make the system flexible. This also helped lead us to the “preview deck” functionality, knowing that students cared about what sort of format these decks were in before downloading. 

### Tie back to the goal
We had some pretty interesting and ambitious ideas. The long duration of this project only made us lose focus even more, spending time on unnecessary and possibly detrimental functionality. We wasted time and effort trying to figure out the “best card” algorithm, despite it being indicated as not important. However, aside from this mishap, by relating other decisions back to our key functionalities, we were able to simplify this project.

### Test early and often
Several rounds of user-testing, along with surveys, allowed us to constantly validate our ideas and product, while also exposing weaknesses in AnkiShare’s usability. 

## Future Plans

### Visual Design
It’s probably clear at this point that we had little to no time working on the visual design of this product. While I recognize the importance of an aesthetically pleasing product, I didn’t hesitate to deliver something visually “acceptable” that worked, given our deadline. Regardless, certain elements such as the typography could be optimized to both enhance usability, scanability, and visual pleasure.

### Scalability
While intended for and limited to medical-school students, flashcards are used by all sorts of people in many different fields. The main concept of AnkiShare is in no way restricted to medicine, and AnkiShare could potentially be expanded and scaled to help other non-medical students as well. 

## Credits
*Endless thanks to the AnkiShare team: Jazmynn Daos, Dillon Gee, Vamsi Koduru, and Kyla Lamontagne.*

### Thanks for your time!





















