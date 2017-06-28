# # # defining a class called Person, which is a type of object
# # class Person(object):
# #     # defining the init method for the class person with a name
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #
# #     def setAge(self, age):
# #         self.age = int(age)
# #
# #     def __str__(self):
# #         ans = self.name + " is age "+ str(self.age)
# #         # return a string
# #         return ans
# #
# #     def getAge(self):
# #         return self.age
# #
# # person1 = Person("Ashlyn", 26)
# # person1.setAge(27)
# # print str(person1)
# #
# # class VSAstudent(Person):
# #     def set_class(self, class_name):
# #         self.class_name = class_name
# #     def get_class(self, class_name):
# #         return self.class_name
# #     def compareAge(self, otherStudent):
# #         if self.age > otherStudent.age:
# #             return self.name + "is older than " + otherStudent.name
# #         else:
# #             return self.name + "is younger than " + otherStudent.name
# #
# # person2 = VSAstudent('Santosh', 15)
# # person2.set_class('programming')
# #
# # print person2
# # print person2.class_name
# #
# # person3 = VSAstudent('Damian', 13)
# #
# # print person2.compareAge(person3)
#
#
#
# class Shape(object):
#     def __init__(self,side):
#         self.side=side
#
# class square(Shape):
#     def findArea(self,side):
#         area=self.side *self.side
#         return area
#
#
# class triangle(Shape):
#     def __str__(self,height):
#         self.height=height
#     def findArea(self,base,height):
#         area=(base*height)*.5
#         return area
#
# s=square(9)
# print s.findArea(s)
#
# t=triangle(1)
# height=4
# base=10
# print t.findArea(base,height)

# Name: Natalie Wright and Arianna Banta
# Date

import feedparser
import string
import time
from project_util import translate_html
from news_gui import Popup

#-----------------------------------------------------------------------
#
# proj08: RSS Feed Filter

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret

#======================
# Part 1
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory(object):
    def __init__(self,guid,title,subject,summary,link):
        self.guid=guid
        self.subject=subject
        self.summary=summary
        self.title=title
        self.link=link

    def get_guid (self):
        return self.guid

    def get_subject (self):
        return self.subject

    def get_summary (self):
        return self.summary

    def get_title (self):
        return self.title

    def get_link (self):
        return self.link


#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError


    # def evaluate(self,guid):



# Whole Word Triggers
# Problems 2-5
#TODO: WordTrigger #trigger
class WordTrigger (Trigger):
    def __init__(self,word):
        self.word=word
    def is_word_in (self,text):
        self.word=self.word.lower()
        text=text.lower()
        #word.upper()
        for item in string.punctuation:
            text=text.replace(item," ")
        text=text.split()
        for word in text:
            if word == self.word:
                return True
        return False






# TODO: TitleTrigger # wordtrigger

class TitleTrigger (WordTrigger,Trigger):
    def evaluate(self, story):
        title=story.get_title()
        return self.is_word_in(title)

# TODO: SubjectTrigger

class SubjectTrigger (WordTrigger,Trigger):
    def evaluate(self, story):
        subject=story.get_subject()
        return self.is_word_in(subject)

# TODO: SummaryTrigger

class SummaryTrigger (WordTrigger,Trigger):
    def evaluate(self, story):
        summary=story.get_summary()
        return self.is_word_in(summary)

# Composite Triggers
# Problems 6-8

# TODO: NotTrigger


class NotTrigger (Trigger):
    def __init__(self,other_trigger):
        self.other_trigger=other_trigger

    def evaluate (self, story):
        other_trigger_answer=self.other_trigger.evaluate(story)
        if other_trigger_answer==True:
            return False
        else:
            return True



    # NotTrigger = N
    # def not(N):evaluate(self, story):
    # return self.is_word_in(N)


# N=story.get_summary()


# TODO: AndTrigger
class AndTrigger (Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        if self.trigger1.evaluate(story) and self.trigger2.evaluate(story):
            return True
        else:
            return False


# TODO: OrTrigger

class OrTrigger (Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        if self.trigger1.evaluate(story) or self.trigger2.evaluate(story):
            return True
        elif self.trigger1.evaluate(story) and self.trigger2.evaluate(story):
            return True
        else:
            return False





# TODO: PhraseTrigger

class PhraseTrigger (Trigger):
    def __init__(self, phrase_trigger):
        self.phrase_trigger = phrase_trigger

    def evaluate(self, story):

        subject = story.get_subject()
        title = story.get_title()
        summary = story.get_summary()

        if self.phrase_trigger in subject:
            return True
        elif self.phrase_trigger in title:
            return True
        elif self.phrase_trigger in summary:
            return True
        else:
            return False



#======================
# Part 3
# Filtering
#======================

def filter_stories(stories, triggerlist):

    storylist=[]

    for story in stories:

        for trigger in triggerlist:

            if trigger.evaluate(story):
                storylist.append(story)

    return storylist







    """
    Takes in a list of NewsStory-s.
    Returns only those stories for whom
    a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    return stories

#======================
# Extensions: Part 4
# User-Specified Triggers
#======================

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """
    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    # TODO: Problem 11
    # 'lines' has a list of lines you need to parse
    # Build a set of triggers from it and
    # return the appropriate ones
    
import thread

def main_thread(p):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    t1 = SubjectTrigger("Kittens")
    t2 = SummaryTrigger("Kittens")
    t3 = PhraseTrigger("Kittens")
    t4 = OrTrigger(t2, t3)
    triggerlist = [t1, t4]
    
    # TODO: Problem 11
    # After implementing readTriggerConfig, uncomment this line 
    #triggerlist = readTriggerConfig("triggers.txt")

    guidShown = []
    
    while True:
        print "Polling..."

        # Get stories from Google's Top Stories RSS news feed
        stories = process("http://news.google.com/?output=rss")
        # Get stories from Yahoo's Top Stories RSS news feed
        stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

        # Only select stories we're interested in
        stories = filter_stories(stories, triggerlist)
    
        # Don't print a story if we have already printed it before
        newstories = []
        for story in stories:
            if story.get_guid() not in guidShown:
                newstories.append(story)
        
        for story in newstories:
            guidShown.append(story.get_guid())
            p.newWindow(story)

        print "Sleeping..."
        time.sleep(SLEEPTIME)

SLEEPTIME = 60 #seconds -- how often we poll
if __name__ == '__main__':
    p = Popup()
    thread.start_new_thread(main_thread, (p,))
    p.start()

