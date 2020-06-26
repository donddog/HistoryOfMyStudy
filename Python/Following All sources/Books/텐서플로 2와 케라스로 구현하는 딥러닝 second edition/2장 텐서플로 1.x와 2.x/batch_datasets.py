import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np

builder = tfds.builder('imdb_reviews')
builder.download_and_prepare()

datasets, info = tfds.load('imdb_reviews', with_info=True, as_supervised=True)

train_dataset = datasets['train']
train_dataset = train_dataset.batch(5).shuffle(50).take(2)

for data in train_dataset:
    print(data)

'''
(<tf.Tensor: shape=(5,), dtype=string, numpy=
array([b'Right from the start you see that "Anchors Aweigh" is a great comedy. Gene Kelly and Frank Sinatra make such a funny team! The songs they sing together are pure entertainment. Kathryn Grayson is gorgeous and really sweet. Dean Stockwell is the cutiest child actor I\'ve never seen. If you are fond of piano, you\'ll be amazed by Jos\xc3\xa9 Iturbi. This movie was the first one to combine animation with real actors and it did that wonderfully in an unforgettable dance number. Undoubtedly one of Kelly\'s funniest movies.',
       b'Why aren\'t more films (especially American) more like Meatball Machine? <br /><br />This is my first official on-line review and I am charged with "electrical ecstasy" after having chosen "Meatball Machine" as my first endeavor. This is a review, so I\'ll try to stick to mere reflection and gut emotion.<br /><br />I mean, this is one creative piece of work even though it is clearly inspired by the now classic TETSUO! So what if it\'s not all original? I own both of these films and though Tetsuo is one strange son of a bitch, Meatball Machine is far superior and can be sat through without the strong desire to indulge in a dose of mind altering drugs to clarify film significance. Meatball Machine is as elaborate in it\'s story as it is in its high influx of blood and gore. Thank you Jesus for Japanese Cinema!<br /><br />Simply put, the last time my dreams were overrun by visions of horror happened after watching Nightmare on Elm Street when I was 7 or so. I could picture in my dreams a tongue coming out of a telephone for weeks on end. This time (at 31) my dreams were pleasantly awe inspiring.<br /><br />In this film human bodies are host to Aliens whose sole purpose is to try and fulfill their never ending quench for human flesh and blood. Humans become flesh eating cyborgs!!! There\'s more!!! Fight scenes!! Great Music!! Great point-of-view shots! Decent acting by the woman Cyborg (at least better than her male counterpart). The fight seen in the end is worth watching ten or twenty times.<br /><br />Oh, and did I forget to mention it\'s a Love story! Wow, I hate love stories but this takes the cake!<br /><br />I can\'t wait to have friends over to watch this film once more just to see the reaction on their faces. Sadly, I took time to write this review because I\'m afraid most friends and family wont understand Meatball Machine. The truth is America as a whole is not prepared for Meatball Machine.<br /><br />Lastly, My wife walked in while I was watching the climactic fight scene at the end and she was speechless. Normally she says something like "why are you watching that junk?" This time she had nothing to say. I was glad! <br /><br />This is not junk. This isn\'t just SPLATTER (splatter for the sake of splatter is also great). This is Art my friends. Art.<br /><br />CHACHO',
       b'I watched \'Ice Age\'in the movie theater and I liked the movie. Spite of the fact that \'Ice Age\'has many flaws and scientific errors,like humans,sabers,dinosaurs and mammoths living at the same period, and even the location of where the story passes(looks North America,but has some characteristics from Iceland for example) we can have fun even so.(unless you are very severe!) <br /><br />The planet is entering an ICE AGE, and many animals are immigrating to the south where is warmer. Sid is a stupid Sloth that is left behind by his own family, that can\'t stand him any longer.Walking in his way, he meets Manfred,or how he calls \'\' Manny\'\' a moody mammoth who does not care about extinction or immigration and is going to the north. Worried that he can easily be captured, Sid decides to follow Manfred, and in the middle of their journey, they found a human mother with her baby. The mother dies but Manfred and Sid decides to take him and return the baby for the humans. Diego, one of the sabers, decides to follow and help them to go to a shortcut to the human\'s camp. What Manfred and Sid does not know, is that Diego is from a saber clan who hates humans and wants to kill the baby, and also pretend to betray they both to make they become saber\'s food. What will happen, will depend of Diego\'s behavior and conscience...<br /><br />aka "A Era do Gelo" - Brazil',
       b'Having not seen all the films released in 2002, I can\'t say that this is the best film of the year. I can say that it is the best film I have seen all year. <br /><br />Most American films featuring black people either obsess over the American preoccupation with "race relations", or fall into the cliches of the inner city ghetto, with every sterotype imaginable spouting ebonic-phrased slang. Antwone Fisher stands proudly alone in this regard: race is irrelevant, save for one fight that may, or may not, have been provoked by a racial slur.<br /><br />Antwone Fisher\'s story is one that should find resonance with any empathic individual. He is understatedly, and thoughtfully, portrayed by Derek Luke. Denzel Washington, while obviously using his star power to have the film made, sticks to the background for the most part, and allows the film to be the Antwone Fisher story. <br /><br />At a time when BET, and popular culture in general want to maintain the ghetoization of a large number of Americans (and Canadians too, you know), this is a film that speaks to the humanity in all of us. I just hope that the non-Black audience will go see this film for that humanity, rather than avoiding it because they feel that there are no characters or actors in the movie whom they can identify with. That would be a sad commentary on race-relations in North America in and of itself. <br /><br />',
       b'In what must be one of the most blood-freezing movies ever, a transvestite is murdering people in New York, and the answer to everything may not be what people suspect. One can see how Brian DePalma takes some influence from Hitchcock with camera angles and stuff. Michael Caine plays a most thought-provoking character, while Angie Dickinson is basically a bored rich woman with a bad hairdo. Keith Gordon (who later starred in "Christine") is probably the most interesting character in the movie. But you can\'t really understand this movie without seeing it. And after seeing it, you may never know just whom you can trust. Also starring Nancy Allen and Dennis Franz.'],
      dtype=object)>, <tf.Tensor: shape=(5,), dtype=int64, numpy=array([1, 1, 1, 1, 1], dtype=int64)>)
(<tf.Tensor: shape=(5,), dtype=string, numpy=
array([b"Living in the Middle East (in Israel), I was excited when I bought my ticket for Syriana. Having seen the trailer, and being a thriller-lover, I expected to see first of all a fast moving, breath catching movie, which wisely dips in global policy-making and the relation between oil, power and corruption, from a fresh angle. Well, I almost left the movie in the middle. The pace was painfully slow, almost all characters were stereotyped, the intertwined editing made understanding the logic very difficult, but, as Steve Rhodes wrote in his review, in the end you don't care. Save your money, save your time, choose another movie.<br /><br />Robi Chernitsky",
       b"I am a huge fan of David Lynch. This film, however, was a quite disappointing experience. Apart from the ambient background music \xc2\x96 which really sets the mood of the film \xc2\x96 it lacks almost all the qualities that I've come to associate with Lynch's work. The visuals are dull, to say the least, and the dialog is to vague and monotone to be of any interest.<br /><br />This feels more like a film students awkward try to do an arty dogma movie than the work of an experienced director. I've seen a lot of amateur movies with far superior camera-work, scenery, sound and script. This film lacks almost all artistic qualities. I feel as though I'm watching one of Davids home videos, produced during a weekend trip with some friends.",
       b"Rated PG-13 for violence, brief sexual humor and drug content. Quebec Rating:13+(should be G) Canadian Home Video Rating:14A<br /><br />I have seen Police Story a couple of times now.In my opinion Police Story is Chan's best film from the 80's.He originally made it because he didn't like the other cop film he had to star in which was The Protector.I have not seen the protector so I cant compare.The acting isn't too bad and the plot is pretty good.I don't remember the plot well because I saw this film a while back but what I do remember is this film has lots of great action,stunts and comedy just what a good Chan film needs.If you can find Police Story and you are Chan fan then buy this film! <br /><br />Runtime:106min <br /><br />9/10",
       b'Saw this \'film\' recently and have to say it was the worst attempt at film making I have ever had the misfortune to see. What the Hell was going on with Coolio? Totally unprovoked shooting at people in distress. Totally uninvolving, slow, tedious and detached. Worse than Spawn. long live "Evil dead II".',
       b'This is the only movie I have ever seen that has prompted me to write a critique on any internet site, and that is a significant statement from someone who likes "The Attack of the Monolith Monsters." This movie is perfect for anyone who wants an inoffensive movie. It is devoid of sex and violence, for example. I believe that this movie is safe for children of all ages. This movie is perfect for anyone who does not want to be entertained, challenged, or stimulated in any way. Adults could easily catch up on their sleep in front of the TV while the kids watch this movie. Don\'t be surprise ,however, if you wakeup to find the kids have turned the TV off and started a board game. As an adult who enjoys being entertained, who enjoys everything from the mundane to the fantastic in realism, drama, comedy, and action, all of those adult things that reflect real life on earth and/or stimulate the imagination, this movie has nothing to offer.'],
      dtype=object)>, <tf.Tensor: shape=(5,), dtype=int64, numpy=array([0, 0, 1, 0, 0], dtype=int64)>)
'''