import streamlit as st
import json
import os

class StudyTracker:
    def __init__(self):
        self.load_progress()
        
        # Complete study plan
        self.months = [
            {
                "title": "MONTH 1-2: DATA STRUCTURES & ALGORITHMS FOUNDATION",
                "weeks": [
                    {
                        "title": "Week 1-2: Arrays & Strings",
                        "tasks": [
                            "Daily: 2 problems from Neetcode.io",
                            "Topic: Two pointer technique",
                            "Topic: Sliding window",
                            "Topic: Prefix sum",
                            "Project: Implement dynamic array from scratch",
                            "Project: Create string matching algorithm",
                            "Weekend: Study different sorting algorithms",
                            "Weekend: Space/time complexity analysis",
                        ]
                    },
                    {
                        "title": "Week 3-4: Hash Tables & Linked Lists",
                        "tasks": [
                            "Daily: 2 problems",
                            "Topic: Hash function implementations",
                            "Topic: Collision resolution",
                            "Topic: Floyd's cycle detection",
                            "Topic: Fast & slow pointer",
                            "Project: Build hashmap from scratch",
                            "Project: Implement LRU cache",
                            "Weekend: Study different hashing techniques",
                            "Weekend: Study doubly linked lists",
                        ]
                    },
                    {
                        "title": "Week 5-6: Trees",
                        "tasks": [
                            "Daily: 2 problems",
                            "Topic: Binary tree traversals",
                            "Topic: BST operations",
                            "Topic: Balanced trees (AVL, Red-Black)",
                            "Topic: Trie implementation",
                            "Project: Build autocomplete system using Trie",
                            "Project: Implement self-balancing BST",
                            "Weekend: Study tree balancing algorithms",
                            "Weekend: Practice complex tree problems",
                        ]
                    },
                    {
                        "title": "Week 7-8: Graphs",
                        "tasks": [
                            "Daily: 2 problems",
                            "Topic: DFS & BFS implementations",
                            "Topic: Shortest path algorithms",
                            "Topic: Minimum spanning trees",
                            "Topic: Union Find",
                            "Project: Social network connection suggester",
                            "Project: Maze solver using different algorithms",
                            "Weekend: Study graph representation methods",
                            "Weekend: Practice advanced graph algorithms",
                        ]
                    }
                ]
            },
            {
                "title": "MONTH 3: ADVANCED ALGORITHMS & SYSTEM DESIGN BASICS",
                "weeks": [
                    {
                        "title": "Week 9-10: Dynamic Programming",
                        "tasks": [
                            "Daily: 2 problems",
                            "Topic: 1D dynamic programming",
                            "Topic: 2D dynamic programming",
                            "Topic: State machines",
                            "Topic: Optimization problems",
                            "Project: Implement a regex matcher",
                            "Project: Create a word break solver",
                            "Weekend: Study DP pattern recognition",
                            "Weekend: Space optimization techniques",
                        ]
                    },
                    {
                        "title": "Week 11-12: System Design Fundamentals",
                        "tasks": [
                            "Study: Designing Data-Intensive Applications (first half)",
                            "Topic: Scalability basics",
                            "Topic: Load balancing",
                            "Topic: Caching strategies",
                            "Topic: Database fundamentals",
                            "Project: Design a URL shortener",
                            "Project: Implement a basic load balancer",
                            "Weekend: Study case studies of real systems",
                            "Weekend: CAP theorem practical applications",
                        ]
                    }
                ]
            },
            {
                "title": "MONTH 4: ADVANCED SYSTEM DESIGN & PYTHON MASTERY",
                "weeks": [
                    {
                        "title": "Week 13-14: Distributed Systems",
                        "tasks": [
                            "Study: Designing Data-Intensive Applications (second half)",
                            "Topic: Distributed transactions",
                            "Topic: Consensus algorithms",
                            "Topic: Message queues",
                            "Topic: Microservices patterns",
                            "Project: Build a distributed counter",
                            "Project: Implement a simple message queue",
                            "Weekend: Study failure modes in distributed systems",
                            "Weekend: Study consistency patterns",
                        ]
                    },
                    {
                        "title": "Week 15-16: Python Internals",
                        "tasks": [
                            "Topic: GIL understanding",
                            "Topic: Memory management",
                            "Topic: Metaclasses",
                            "Topic: Decorators",
                            "Topic: Context managers",
                            "Project: Custom decorator library",
                            "Project: Memory profiler tool",
                            "Weekend: Python optimization techniques",
                            "Weekend: Advanced Python features",
                        ]
                    }
                ]
            },
            {
                "title": "MONTH 5: CLOUD & DEVOPS",
                "weeks": [
                    {
                        "title": "Week 17-18: AWS Deep Dive",
                        "tasks": [
                            "Topic: VPC design",
                            "Topic: ECS/EKS",
                            "Topic: Lambda architecture",
                            "Topic: S3 optimization",
                            "Topic: RDS management",
                            "Project: Serverless API",
                            "Project: Auto-scaling application",
                            "Weekend: Cost optimization",
                            "Weekend: Security best practices",
                        ]
                    },
                    {
                        "title": "Week 19-20: Kubernetes & CI/CD",
                        "tasks": [
                            "Topic: Kubernetes architecture",
                            "Topic: Pod lifecycle",
                            "Topic: Service mesh",
                            "Topic: GitOps practices",
                            "Project: Multi-service application deployment",
                            "Project: Custom Kubernetes operator",
                            "Weekend: Monitoring and logging",
                            "Weekend: Deployment strategies",
                        ]
                    }
                ]
            },
            {
                "title": "MONTH 6: INTERVIEW PREPARATION & PRACTICE",
                "weeks": [
                    {
                        "title": "Week 21-22: Mock Interviews & System Design Practice",
                        "tasks": [
                            "Daily: 1 mock coding interview",
                            "Daily: 1 system design practice",
                            "Topic: Communication skills",
                            "Topic: Problem-solving approach",
                            "Topic: System design patterns",
                            "Weekend: Practice performance under pressure",
                            "Weekend: Implement feedback",
                        ]
                    },
                    {
                        "title": "Week 23-24: Final Polish",
                        "tasks": [
                            "Review weak areas from previous months",
                            "Practice behavioral questions",
                            "Build portfolio of projects",
                            "Document achievements and metrics",
                            "Mock interviews with peers",
                        ]
                    }
                ]
            }
        ]
        
    def load_progress(self):
        """Load saved progress from file"""
        if os.path.exists('progress.json'):
            with open('progress.json', 'r') as f:
                self.completed = json.load(f)
        else:
            self.completed = {}

    def save_progress(self):
        """Save progress to file"""
        with open('progress.json', 'w') as f:
            json.dump(self.completed, f)

    def display_tracker(self):
        """Display the study tracker interface"""
        st.title("6-Month Study Plan Tracker")
        
        for month_idx, month in enumerate(self.months):
            st.header(month["title"])
            
            for week_idx, week in enumerate(month["weeks"]):
                with st.expander(f"{week['title']} - Progress: {self.get_progress(month_idx, week_idx, week['tasks'])}/{len(week['tasks'])} tasks"):
                    for task_idx, task in enumerate(week["tasks"]):
                        key = f"{month_idx}-{week_idx}-{task_idx}"
                        completed = st.checkbox(
                            task,
                            key=key,
                            value=self.completed.get(key, False)
                        )
                        if completed != self.completed.get(key, False):
                            self.completed[key] = completed
                            self.save_progress()

    def get_progress(self, month_idx, week_idx, tasks):
        """Calculate progress for a given week"""
        completed_tasks = 0
        for task_idx in range(len(tasks)):
            key = f"{month_idx}-{week_idx}-{task_idx}"
            if self.completed.get(key, False):
                completed_tasks += 1
        return completed_tasks

def main():
    st.set_page_config(page_title="Study Tracker", layout="wide")
    tracker = StudyTracker()
    tracker.display_tracker()

if __name__ == "__main__":
    main()