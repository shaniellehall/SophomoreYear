"""
Author: Shanielle Hall
Date: November 26, 2025
Description: GraduationCeremony class for managing commencement ceremonies
"""

from queue import PriorityQueue, Queue, LifoQueue
from participants import Participant, Graduate


class LinkedListNode:
    """Node for linked list"""
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        """String representation showing chain of nodes"""
        result = str(self.data)
        if self.next is not None:
            result += " --> " + str(self.next)
        else:
            result += " --> None"
        return result


class LinkedList:
    """Simple linked list implementation"""
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        """Add item to end of list"""
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


class GraduationCeremony:
    """Manages a university commencement ceremony"""
    
    def __init__(self, university, date):
        """Initialize graduation ceremony with university name and date"""
        self.__university = university
        self.__date = date
        self.__speakers = PriorityQueue()
        self.__graduates = Queue()
        self.__undergraduates = Queue()
        self.__stageParty = LifoQueue()
        self.__photoManifest = LinkedList()
        self.__speakerCount = 0
    
    def addGraduate(self, graduate):
        """Add a graduate to the appropriate queue based on designation"""
        if graduate.getDesignation() == "G":
            self.__graduates.put(graduate)
        else:  # "UG"
            self.__undergraduates.put(graduate)
    
    def addSpeaker(self, speaker, priority):
        """Add a speaker to the priority queue"""
        self.__speakers.put((priority, self.__speakerCount, speaker))
        self.__speakerCount += 1
    
    def addStagePartyMember(self, participant):
        """Add a participant to the stage party stack"""
        self.__stageParty.put(participant)
    
    def hasNextSpeaker(self):
        """Check if there are any speakers waiting"""
        return not self.__speakers.empty()
    
    def getNextSpeaker(self):
        """Dequeue and return next speaker, add to photo manifest"""
        if self.hasNextSpeaker():
            _, _, speaker = self.__speakers.get()
            self.__photoManifest.append(speaker)
            return speaker
        return None
    
    def hasNextGraduate(self):
        """Check if there are any graduates waiting"""
        return not self.__graduates.empty() or not self.__undergraduates.empty()
    
    def getNextGraduate(self):
        """Dequeue and return next graduate (G before UG), add to photo manifest"""
        if not self.__graduates.empty():
            graduate = self.__graduates.get()
            self.__photoManifest.append(graduate)
            return graduate
        elif not self.__undergraduates.empty():
            graduate = self.__undergraduates.get()
            self.__photoManifest.append(graduate)
            return graduate
        return None
    
    def getRecessional(self):
        """Return list of stage party members in reverse order"""
        recessional = []
        while not self.__stageParty.empty():
            participant = self.__stageParty.get()
            recessional.append(participant.getFullName())
        return recessional
    
    def getPhotoManifest(self):
        """Return head of linked list photo manifest"""
        return self.__photoManifest.head
    
    def getNumParticipants(self):
        """Return total number of participants in ceremony"""
        total = 0
        total += self.__speakers.qsize()
        total += self.__graduates.qsize()
        total += self.__undergraduates.qsize()
        total += self.__stageParty.qsize()
        return total
    
    def getProgramText(self):
        """Generate formatted program text without altering data structures"""
        lines = []
        lines.append(f"{self.__university} Commencement Ceremony")
        lines.append(self.__date)
        lines.append("")
        
        # Collect speakers without removing them
        speakers_list = []
        temp_queue = PriorityQueue()
        while not self.__speakers.empty():
            item = self.__speakers.get()
            speakers_list.append(item)
            temp_queue.put(item)
        # Restore speakers queue
        while not temp_queue.empty():
            self.__speakers.put(temp_queue.get())
        
        lines.append("Speakers:")
        for _, _, speaker in speakers_list:
            lines.append(f"- {speaker}")
        lines.append("")
        
        # Collect and sort graduate students
        grad_list = []
        temp_queue = Queue()
        while not self.__graduates.empty():
            grad = self.__graduates.get()
            grad_list.append(grad)
            temp_queue.put(grad)
        # Restore graduates queue
        while not temp_queue.empty():
            self.__graduates.put(temp_queue.get())
        
        # Sort graduate students alphabetically
        for i in range(len(grad_list)):
            for j in range(i + 1, len(grad_list)):
                if grad_list[i].getSortName() > grad_list[j].getSortName():
                    grad_list[i], grad_list[j] = grad_list[j], grad_list[i]
        
        lines.append("Graduate Students:")
        for grad in grad_list:
            lines.append(f"- {grad}")
        lines.append("")
        
        # Collect and sort undergraduate students
        undergrad_list = []
        temp_queue = Queue()
        while not self.__undergraduates.empty():
            undergrad = self.__undergraduates.get()
            undergrad_list.append(undergrad)
            temp_queue.put(undergrad)
        # Restore undergraduates queue
        while not temp_queue.empty():
            self.__undergraduates.put(temp_queue.get())
        
        # Sort undergraduate students alphabetically
        for i in range(len(undergrad_list)):
            for j in range(i + 1, len(undergrad_list)):
                if undergrad_list[i].getSortName() > undergrad_list[j].getSortName():
                    undergrad_list[i], undergrad_list[j] = undergrad_list[j], undergrad_list[i]
        
        lines.append("Undergraduate Students:")
        for undergrad in undergrad_list:
            lines.append(f"- {undergrad}")
        
        return "\n".join(lines)
