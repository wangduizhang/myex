#_*_coding:utf-8
import feedparser #辅助提取和分裂信息文本
import string
import time
from project_util import translate_html
from Tkinter import *


#-----------------------------------------------------------------------
#
# Problem Set 7

#======================
# Code for retrieving and parsing RSS feeds
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

#======================
# Part 1
# Data structure design
#======================

# Problem 1
class NewsStory(object):
    """docstring for NewsStory"""
    def __init__(self, Guid, Title, Subject, Summary, Link):
        self.Guid = Guid
        self.Title = Title
        self.Subject = Subject
        self.Summary = Summary
        self.Link = Link
    def getGuid(self):
        return self.Guid
    def getTitle(self):
        return self.Title
    def getSubject(self):
        return self.Subject
    def getSummary(self):
        return self.Summary
    def getLink(self):
        return self.Link

#======================
# Part 2
# Triggers
#======================
def str_replace(str_):
    for i in string.punctuation:
        newstr_ = str_.replace(i,' ')
        str_ = newstr_
    return newstr_ 


class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError


class WordTrigger(Trigger):
    """docstring for WordTrigger"""
    def __init__(self, word):
        self.word = word
    def isWordIn(self,text):
        newtext = str_replace(text)
        words = newtext.split()
        for i in words:
            if i.lower() == self.word.lower() and i != ' ':
                return True
        return False
        

class TitleTrigger(WordTrigger):
    def evaluate(self,story):
        newstory = str_replace(story.Title)
        words = newstory.split()
        for i in words:
            if i.lower() == self.word.lower() and i != ' ':
                return True
        return False


class SubjectTrigger(WordTrigger):
    def evaluate(self,story):
        newstory = str_replace(story.Subject)
        words = newstory.split()
        for i in words:
            if i.lower() == self.word.lower() and i != ' ':
                return True
        return False


class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        newstory = str_replace(story.Summary)
        words = newstory.split()
        for i in words:
            if i.lower() == self.word.lower() and i != ' ':
                return True
        return False


# Problems 6-8

# TODO: NotTrigger
class NotTrigger(Trigger):
    """docstring for NotTrigger"""
    def __init__(self,mou_):
        self.mou_ = mou_
    def evaluate(self,new):
        return  not self.mou_.evaluate(new)


class AndTrigger(Trigger):
    """docstring for AndTrigger"""
    def __init__(self, mou_1, mou_2):
        self.mou_1 = mou_1
        self.mou_2 = mou_2
    def evaluate(self,new):
        return self.mou_1.evaluate(new) and self.mou_2.evaluate(new)



class OrTrigger(Trigger):
    """docstring for OrTrigger"""
    def __init__(self, mou_1, mou_2):
        self.mou_1 = mou_1
        self.mou_2 = mou_2
    def evaluate(self,new):
        return self.mou_1.evaluate(new) or self.mou_2.evaluate(new)
        


# Question 9

# TODO: PhraseTrigger
def judge_(parse, new):
    phrasecase = []
    for i in  range(len(new)):
        if new[i] == parse[0]:
            phrasecase.append(new[i:])
    if len(phrasecase) == 0:
        return False
    for p in phrasecase:
        if p[0:len(parse)] == parse:
            return True
    return False


class PhraseTrigger(Trigger):
    """docstring for PhraseTrigger"""
    def __init__(self,parse):
        self.parse = parse 
    def evaluate(self,new):
        return judge_(self.parse, new.Title) or judge_(self.parse, new.Subject) or judge_(self.parse, new.Summary)



#======================
# Part 3
# Filtering
#======================

def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    nstories = []
    for s in stories:
        for t in triggerlist:
            if t.evaluate(s):
                nstories.append(s)
                break
    return nstories 
#======================
# Part 4
# User-Specified Triggers
#======================

def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.

    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")

    Modifies triggerMap, adding a new key-value pair for this trigger.

    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).
    """
    # TODO: Problem 11


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

    triggers = []
    triggerMap = {}

    # Be sure you understand this code - we've written it for you,
    # but it's code you should be able to write yourself
    for line in lines:

        linesplit = line.split(" ")

        # Making a new trigger
        if linesplit[0] != "ADD":
            trigger = makeTrigger(triggerMap, linesplit[1],
                                  linesplit[2:], linesplit[0])

        # Add the triggers to the list
        else:
            for name in linesplit[1:]:
                triggers.append(triggerMap[name])

    return triggers
    
import thread

SLEEPTIME = 60 #seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    try:
        # These will probably generate a few hits...
        t1 = TitleTrigger("Obama")
        t2 = SubjectTrigger("Romney")
        t3 = PhraseTrigger("Election")
        t4 = OrTrigger(t2, t3)
        triggerlist = [t1, t4]
        
        # TODO: Problem 11
        # After implementing makeTrigger, uncomment the line below:
        # triggerlist = readTriggerConfig("triggers.txt")

        # **** from here down is about drawing ****
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)
        
        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)

        # Gather stories
        guidShown = []
        def get_cont(newstory):
            if newstory.getGuid() not in guidShown:
                cont.insert(END, newstory.getTitle()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.getSummary())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.getGuid())

        while True:

            print "Polling . . .",
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

            # Process the stories
            stories = filterStories(stories, triggerlist)

            map(get_cont, stories)
            scrollbar.config(command=cont.yview)


            print "Sleeping..."
            time.sleep(SLEEPTIME)

    except Exception as e:
        print e


if __name__ == '__main__':

    root = Tk()
    root.title("Some RSS parser")
    thread.start_new_thread(main_thread, (root,))
    root.mainloop()

