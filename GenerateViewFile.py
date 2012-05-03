#! python2.7
## -*- coding: utf-8 -*-

## kun for apk view tracing
## GenerateViewFile.py

from BuildTree import build
from GlobalVariable import click_action_list,touch_action_list,drag_action_list,Action_Sequence_Map

def getViewCenterPoint(node):
    width = node.mAbsoluteRect.mRight - node.mAbsoluteRect.mLeft
    height = node.mAbsoluteRect.mBottom - node.mAbsoluteRect.mTop
    pointX = node.mAbsoluteRect.mLeft + width/2
    pointY = node.mAbsoluteRect.mTop + height/2    
    return pointX,pointY


def generateViewPointList(tree_nodes_list):
    view_point_list=[]
    
    for node in tree_nodes_list:
        if node.mActive:
            view_point_list.append(getViewCenterPoint(node))
            
    print view_point_list
    return view_point_list


## generate view file named "***.vf"
## not implement yet
def generateViewFile(view_point_list, file_name):
    view_file = open(file_name, "w")
    
    ## click events sequence
    for view_point in view_point_list:
        view_file.write(str(view_point[0])+"|"+str(view_point[1])+"\n")
        
    try:
        view_file.close()
    except Exception,e:
        print "Failed to close the view file! [Error] %s " %str(e)

## return list in memory
def generateActionList(view_point_list):
    action_sequence_list=[]

    return action_sequence_list
    

def main():
    tree_nodes_list = build()
    view_point_list = generateViewPointList(tree_nodes_list)
    #generateActionList(view_point_list)
    generateViewFile(view_point_list, "demo.vf")


if __name__=="__main__":
    main()
