#!/usr/bin/env python
# coding: utf-8

# In[103]:





# In[207]:


class Bst:
    class Node:
        def __init__(self, data):
            self.data = data
            self.r_child = None
            self.l_child = None
    def __init__(self):
        self.root = None

    def insert_binary(self,root,child_node):
        if root is None:
            root = child_node            
        else:
            if root.data > child_node.data:
                if root.l_child is None:
                    root.l_child = child_node
                else:
                    self.insert_binary(root.l_child, child_node)
                    
            else:
                if root.r_child is None:
                    root.r_child = child_node
                else:
                    self.insert_binary(root.r_child, child_node)
                    
    
    def in_order_traversal(self, root):
        if not root:
            return 'No root provided'
        self.in_order_traversal(root.l_child)
        print(root.data)
        self.in_order_traversal(root.r_child)


# In[208]:


r = Node(3)


# In[209]:


tree = Bst()


# In[210]:


tree.insert_binary(r, Node(2))


# In[211]:


tree.insert_binary(r, Node(4))


# In[212]:


tree.insert_binary(r, Node(1))


# In[213]:


tree.insert_binary(r, Node(6))


# In[214]:


tree.in_order_traversal(r)


# In[181]:


tree.insert_binary(r, Node(5))


# In[177]:


r.r_child.data


# In[178]:


r.l_child.l_child.data


# In[179]:


r.r_child.r_child.data


# In[193]:


r.r_child.r_child.l_child.data


# In[ ]:




