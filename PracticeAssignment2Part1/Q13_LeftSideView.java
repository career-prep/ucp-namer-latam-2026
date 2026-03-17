package PracticeAssignment2Part1;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Q13_LeftSideView {
    class Node{
        int data;
        Node left;
        Node right;
        Node(int data){
            this.data = data;
            left = null;
            right = null;

        }
        public List<Integer> leftView(Node root){
            if(root==null){
                return new ArrayList<>();
            }
            /**
             * my approach here is going through the tree using level order ,storing it in the list, since its left side view the left element will always be the first element stored
             * currently in the Queue. So i get the first elemnt ,store it in the result list and remove all current element in the currnt queue that stores the nodes at that level;
             * 
             */
            List<Integer> resultList = new ArrayList<>();//stores the leftside viewed integers
            Queue<Node> levelQueue = new LinkedList<>(); // stores nodes at current level
            levelQueue.add(root);
            while(!levelQueue.isEmpty()){
                int size = levelQueue.size();// keeping track of size so we only store one node data from each level and delte only that levels node
                Node resultNode = levelQueue.poll();
                 resultList.add(resultNode.data);//adding first node in levelQueue because its leftSideView
                 // adding any childeren this node may have
                if(resultNode.left!=null){
                        levelQueue.add(resultNode.left);
                    }
                if(resultNode.right!=null){
                        levelQueue.add(resultNode.right);
                    }
                for(int i=0;i<size-1;i++){//deletes the current nodes at the current level
                    Node temp = levelQueue.poll();
                    if(temp.left!=null){
                        levelQueue.add(temp.left);
                    }
                    if(temp.right!=null){
                        levelQueue.add(temp.right);
                    }

                }
               
            }
            return resultList;

        }
    }
}
