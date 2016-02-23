---
layout: writeup
title: AnkiShare
intro: Providing reliable study material for medical students.
details: UX Research/Design
---

- Capstone Project in Informatics at U.C. Irvine
- 9-month duration
- I was responsible for the research, mockups, and user-testing.

## Background

Our client, a student in medical school, wanted an application that allowed students to easily share their <a href='http://ankisrs.net'>Anki</a> flash cards:

> The app connects everyone’s Anki accounts, pooling all their cards in the database. Students can access this database. App has algorithms that can identify the _best_ cards for any given category, consolidating them into ‘master decks.’

Basically, it:

- Connects everyone’s Anki accounts
- Gives access to other people’s cards
- Finds the “best cards” per category

He also described some pain-points he was trying to address:

- Annoying and tedious to send flashcards (the logistics of it all)
- Deck availability limited to who you knew (especially relevant to incoming students)
- Awkward to ask your peers for their decks

## Research & Requirements

We started with research, which involved getting to know both the **users*** and the **Anki software** that we would be building for, to both better understand their pain-points as well as their contexts.

**Our client specified that this application would be limited to students of the U.C. Irvine School of Medicine.*

### Anki Software
We downloaded the Anki desktop/mobile applications, and found some decks to play around with. 

- Software included on every incoming student’s iPad 
- Anki decks must be added to a user’s library within the <i>desktop</i> app, and can be synced to devices from there (similar to puttings songs on your iPod via iTunes back in the day)
- There is a built-in learning algorithm (hence its popularity with students, as we later confirmed)
- Code for the desktop-app *not* available

### Surveys
Access to all 400-ish students was available through their mailing list. This allowed us to send them surveys throughout the course of this project. 

We used these to validate our assumptions and mission.

- All students use Anki cards
- Most (90%+) students shared cards with their peers*
- They spend *a lot* of time studying. 
- Students study on their laptops and iPads
- Students often collaborated in making/improving decks

**This was important to us, as a common argument was “isn’t most of the value in the making of the cards?” 

### Contextual Inquiry 
These surveys also helped us meet with some students. They walked us through their file libraries, and talked about their study habits and flashcard preferences. 

- Most students had 1,000–20,000 cards in their libraries
- Everyone categorized/labelled their decks differently
- Similarly, everyone’s cards were in different formats*

**We think of flashcards as question on the front, answer on the back. This was not the case at all. Many consisted of only images, and one or two words.*

### Personas
With this information and interaction with the users, we identifed two personas that these students almost all fell into: the **downloader**, and the **uploader**. 

<img src="/files/ankishare_personas.png" data-action="zoom">


This resulted in the idea of our two **key functionalities**: uploading and downloading.

### Research Summary

- The **Value** of the product lies in two main areas:
  1. Saves valuable time spent communicating between students and sending decks
  2. Makes a vast wealth of resources available
- The **User’s environment** is a combination of iPad and laptop — decks have to be imported via the desktop app, so we will be building a web-application.
- **Anki Decks** are numerous and diverse in both content and format
- **UCI School of Medicine** has a set curriculum — all students of any given year take the same classes

## Design
 
At this point, it was relatively clear what AnkiShare was going to be.

- **Repository of cards** was a pretty simple concept to us — basically just a huge dump of cards that was nicely categorized.
- **Best Cards Algorithm** was something else, and the greatest design challenge we faced.

### “Best Card”
 At the beginning of the project, we had identified that the technical skill amongst our team was not very strong at all. Yet, we still entertained ideas regarding image-recognition, machine learning, and other things that will one day take over the world. 

Our client suggested grouping all similar/redundant cards together, and figuring out how to identify the best card for each group, aggregating all of *these* cards into the so-called “master deck.” Something like this:

- ALL CARDS
  - Anatomy 101 cards
    - Cards about the number of bones in the hand
    	- *Best* card about number of bones in the hand

This *best* card would then be put into a *master* Anatomy 101 deck with all the other *best* cards.

Our research showed that this would be impossible. Cards were in various formats, half of them not including any text. Content was generally the same, but not the formatting. It would be like comparing apples to apple pie — not actually comparable.

We weren’t going to give up that easily, though. While no algorithm could rank these cards, *people* could — Our *users* could. 

I looked to real products that also promote content based on popularity among their users.<a href='http://reddit.com'>Reddit</a>’s upvote/downvote system was one that we thought about, along with <a href='http://yelp.com'>Yelp</a>’s star-based rating system.

<img src="/files/ankishare_bestcard.png" data-action="zoom">

The mockup above represents just one of *many* ideas we considered, imagining every possible way this could be achieved. I started to question whether or not this was even something we should have conisdered. Referring back to our initial goals and requirements, the value did *not* actually lie in this functionality. We wanted to *save* students time, not have them spend *more* time voting on cards.

However, this was met with some resistance both within the team and from the client. This functionality was important to them, in the supposed extra value it presented. Additionally, a fancy algorithm would boost the “cool-factor” of AnkiShare — not something to seriously consider.

As a compromise, I suggested tracking the number of times a deck is downloaded, as a proxy for its popularity, and by extension, quality. While obviously a far cry from optimizing at the card level, the trade-off 

## Repository Structure
During that ordeal, we were also thinking of ways to structure our deck “repository.” Our research showed that students would generally know what decks they were looking for, whether it be “material for Professor X’s Anatomyy final,” or “Histology 101, Week 3.” This translated into us needing an intuitive, precise, structure that could **let students easily pinpoint what they had in mind**.

However, upon looking at many existing decks created by students, we noticed that there were many ways they were classified — some people made decks by course, some by topic, some by exam. This suggested several possible “directory structures,” such as:

<img src="/files/ankishare_hierarchy_example.png" data-action="zoom">

It ultimately meant that there was no one structure that could account for all these different decks. I instead decided to not categorize them at all, and implement a filter.

<img src="/files/ankishare_filter.png" data-action="zoom">

A filter seems like the obvious solution, but wasn’t an option when we were still considering having “master decks.”

## Key Functionality
We were finally able to narrow down the product to a simple DropBox-esque web application, that allowed students to **upload** and **download** files. 

## User Testing
To validate our product, test its usability, and receive feedback, we scheduled several rounds of user testing with medical students. 

Going in, I prepared a list of questions and tasks for students to complete. We defined success based on how quickly and easily they could perform these tasks. Watching even the most confident students struggle with the simplest of tasks was definitely a reality check for us. In addition to issues with the interface and layout, we were able to identify confusing copy, and incorrect assumptions.  

- **Ambiguous terminology** in our copy. For example, students didn’t know if “author” referred to the student who made the deck or the professor who wrote the textbook that the cards are based off of. We started including this in our surveys, to decide on which nomenclature to use.
- **The interface was confusing** to some. The most eye-opening to me was when we had a case of a <a href='https://www.nngroup.com/articles/illusion-of-completeness/'>false floor</a>. The student selected her filter fields, and the content appeared below the fold. She never noticed that it was there, and stared blankly back at me. This was fixed by including a “Filter” action button instead of an auto-filter, and slightly modified sizing.
- **Clutter on the filter** was brought up many times, and hindered our testers’ ability to quickly locate a given deck. At the time, we were including every single course the school offers under the “course” filter. I hypothesized that students would only be looking for courses corresponding to their given year, and after surveys, I was actually right. We modified the filter to only showing the courses of the user’s year, *reducing 75% of the clutter*.

Fortunately, the high-level concept of our product (“It’s basically a DropBox for Anki decks”) was easily understood and clear. Students realized the value and basic workflow/functionality of the product. 

### Viewing & Editing
While students could easily download the deck that we specified, many expressed concerns for knowing which deck to download. They elaborated that when looking for decks, they want to know what they’re getting. **Card format and “style” were much more important to them than we expected.** Because of this, we quickly threw together a “Deck Preview” feature that allowed them to view the decks in their entirety before downloading. With this new functionality, we this new viewing interface, the plug-in we used also afforded us easy implementation of an “edit” function, promoting collaboration among the students in improving these decks.

## Final Product
The final product was infinitely simpler than we could have ever expected, but effectively carried out its twin key functionalities: **upload** and **download**. 

<img src="/files/ankishare_upload.png" data-action="zoom">

<img src="/files/ankishare_download.png" data-action="zoom">

## What we learned

### Design with real data/content
If we hadn’t seen the wide variety of deck formats, we would have likely assumed that flashcards were all Question Text/Answer Text. Luckily, we had plenty of access to real users and their files, and could make the system flexible. This also helped lead us to the “preview deck” functionality, knowing that students cared about what sort of format these decks were in before downloading. 

### Tie back to the goal
We had some pretty interesting and ambitious ideas. The long duration of this project only made us lose focus even more, spending time on unnecessary and possibly detrimental functionality. By tying everything back to the main goal of sharing flash-cards, we were able to narrow down our scope and focus on our two core functions.

### Test early and often
Several rounds of user-testing, along with surveys, allowed us to constantly validate our ideas and product, while also exposing weaknesses in AnkiShare’s usability. 

## Future Plans

### Visual Design
It’s probably clear at this point that we had little to no time working on the visual design of this product. While I recognize the importance of an aesthetically pleasing product, I didn’t hesitate to deliver something visually “acceptable” that worked, given a deadline. Regardless, certain elements such as the typography could be optimized to both enhance usability, scannability, and visual pleasure.

### Scalability
While intended for and limited to medical-school students, flashcards are used by all sorts of people in many different fields. The main concept of AnkiShare is in no way restricted to medicine, and AnkiShare could potentially be expanded and scaled to help other non-medical students as well. 

## Credits
*Endless thanks to the AnkiShare team: Jazmynn Daos, Dillon Gee, Vamsi Koduru, and Kyla Lamontagne.*

### Thanks for your time!





















