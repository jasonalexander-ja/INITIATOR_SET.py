<<<<<<< Updated upstream
=======
# Miscillaneous utility methods and classes for general use
# Contributing authors: 
#  -Lucianna Osucha (lucianna@vulpinedesings.com)

import sys



class RobustLinkedList:
  class ListNode:
    def __init__(self, data, n_next=None, n_prev=None):
      self.data = data
      self.prev = n_prev
      self.next = n_next

    def __str__(self):
      return str(self.data)

  def __init__(self, curNode=None, n_head=None, n_foot=None, size=-1):
    self.curNode = curNode
    
    if curNode != None:
      if n_head == None:
        n_head = curNode
      if n_foot == None:
        n_foot = curNode

    self.foot = n_foot
    self.head = n_head
    self.size = size

    getSize()

  @classmethod
  def from_list(cls, m_list):
    head = RobustLinkedList.ListNode(m_list[0])
    cur = head

    for i in range(1, len(m_list)):
      cur.next = RobustLinkedList.ListNode(m_list[i], None, cur)
      cur = cur.next
    
    return cls(head, head, cur, len(m_list))


  def setData(self, data, force=False):
    self.validate(force).data = 


  def getData(self, force=False):
      return self.validate(force=False).data

  def validate(self, rebuild=False):
    if self.curNode == None:
      print("Current node unset, attempting return to head")
      if self.head == None:
        print("Head unset, attempting set to foot")
        if self.foot == None:
          if rebuild:
            print("Foot unset. Adding empty node...")
            self.curNode = RobustLinkedList.ListNode(None)
            return self.curNode
          else:
            print("Foot unset. Returning...")
            return None
        else:
          print ("Foot found!")
          if rebuild:
            rebuildIndex(True)
            return self.curNode
          else:
            self.head = self.foot
            self.curNode = self.foot
            return self.curNode
      else:
        rebuildIndex()
        return self.curNode
    else:
      return self.curNode


  def rebuildIndex(backwards=False):
    output = "Attempting to rebuild from "
    if backwards:
      output += "foot"
    else:
      output += "head"
    print(output + "...")

    if backwards and self.foot == None:
      return False
    else if !backwards and self.head == None
      return False

    if backwards:
      self.curNode = self.foot
      while self.curNode.prev != None:
        self.curNode.next.prev = self.curNode
    else:
      self.curNode = self.foot


  def insert(self, data, priorTo=False, ignoreType=False):
    if !ignoreType and isinstance(data, list):
      data = from_list(data)

    if !ignoreType and isinstance(data, RobustLinkedList):
      if self.size == 0:
        self.curNode = data.curNode
        self.head = data.head
        self.foot = data.foot
        self.size = data.size
      else:
        if len(data) == -1:
          self.size = -1
        else:
          self.size += len(data)
      if priorTo:
        data.foot.next = self.curNode
        data.head.prev = self.curNode.prev
        if self.curNode.prev == None:
          self.head = data.head
        else:
          self.curNode.prev.next = data.head
        self.curNode.prev = data.foot
      else:
        data.head.prev = self.curNode
        data.foot.next = self.curNode.next
        if self.curNode.next == None:
          self.foot = data.foot
        else:
          self.curNode.next.prev = data.foot
        self.curNode.next = data.head

    else:
      if self.size == 0:
        self.curNode = RobustLinkedList.ListNode(data)
        self.head = self.curNode
        self.foot = self.curNode
      else:
        if priorTo:
          newNode = RobustLinkedList.ListNode(data, self.curNode, self.curNode.prev)
          if self.curNode.prev == None:
            self.head = newNode
          self.curNode.prev = newNode
        else:
          newNode = RobustLinkedList.ListNode(data, self.curNode.next, self.curNode)
          if self.curNode.next == None:
            self.foot = newNode
          self.curNode.next = newNode
        self.curNode = newNode
      self.size += 1
    return self



  def remove(self):
    if self.head == self.foot:
      self.head = None
      self.foot = None
      self.curNode = None
      self.size = 0
      return self

    elif self.curNode.prev == None:
      self.head = self.curNode.next
      self.curNode = self.head
      self.curNode.prev = None
    elif self.curNode.next == None:
      self.foot = self.curNode.prev
      self.curNode = self.foot
      self.curNode.next = None
    else:
      self.curNode.prev.next = self.curNode.next
      self.curNode.next.prev = self.curNode.prev
      self.curNode = self.curNode.next
    self.size -= 1
    return self


  def __len__(self):
    return self.getSize()

  def getSize(self, forceRecalc=False):
    if forceRecalc or size == -1:
      print("Recaculating size...")
      node = self.head
      self.size = 0;
      while node != None:
        self.size += 1
        node = node.next
        if (self.size > 10000): # Assume loop at 10,000 iterations
          self.size = -1
          break
    return self.size

  def to_head(self):
    self.curNode = self.head
    return self

  def to_foot(self):
    self.curNode = self.foot
    return self

  def at_head(self):
    if self.curNode.prev == None:
      if self.curNode != self.head:
        self.head = self.curNode
        self.getSize(True)
      return True
    else:
      return False

  def at_foot(self):
    if self.curNode.next == None:
      if self.curNode != self.foot:
        self.foot = self.curNode
        self.getSize(True)
      return True
    else:
      return False

  def next(self):
    if self.at_foot():
      return None
    else:
      self.curNode = self.curNode.next
      return self.getData()
  
  def prev(self):
    if self.at_head():
      return None
    else:
      self.curNode = self.curNode.prev
      return self.getData()

  # Traverse n entries, positive values go footwards and negatives go headwards.
  def traverse(self, n = 1):
    while n > 0:
      self.curNode = self.curNode.next
      if (self.curNode == None):
        self.curNode = self.head
      n -= 1
    
    while n < 0:
      self.curNode = self.curNode.prev
      if (self.curNode == None):
        self.curNode = self.foot
      n += 1

    return self

  def __str__(self):
    node = self.head
    result = ""
    while node != None:
      if node == self.curNode:
        result += "-> " + str(node) + "\n" 
      else:
        result += "   " + str(node) + "\n"
      node = node.next
    return result
>>>>>>> Stashed changes



# Find index in a sorted list. If not found, returns the negated index of the
# nearest value #TODO
def stubbornBinSearch(list, object) -> int:
	i = list.len() / 2
	j = 0
	while (list[i] != object && i != j):
		
  return ((i == j) * -1) * i;
