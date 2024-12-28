import streamlit as st
import json
import os
from datetime import datetime, timedelta

class StudyTracker:
    def __init__(self):
        self.load_progress()
        
        # Define daily schedule template for each week type
        self.daily_schedules = {
            "DSA_WEEK": {
                "Monday": ["2 Leetcode problems", "Study core theory", "Practice implementations"],
                "Tuesday": ["2 Leetcode problems", "Deep dive into concepts", "Solve medium problems"],
                "Wednesday": ["2 Leetcode problems", "Advanced theory", "Build helper functions"],
                "Thursday": ["2 Leetcode problems", "Pattern practice", "Optimize solutions"],
                "Friday": ["2 Leetcode problems", "Mock interviews", "Project work"],
                "Saturday": ["Review all patterns", "Major project work", "Extra practice"],
                "Sunday": ["Weekly review", "Prepare next week", "Rest and reflect"]
            },
            "SYSTEM_DESIGN_WEEK": {
                "Monday": ["Read chapter", "System design problem", "Research components"],
                "Tuesday": ["Study examples", "Design document", "Implementation plan"],
                "Wednesday": ["Deep dive topic", "Architecture review", "Component design"],
                "Thursday": ["Case studies", "Scale considerations", "Trade-off analysis"],
                "Friday": ["Mock design interview", "Document design", "Review feedback"],
                "Saturday": ["Implementation work", "Testing strategy", "Performance analysis"],
                "Sunday": ["Weekly review", "Prepare next week", "Rest and reflect"]
            },
            "CLOUD_WEEK": {
                "Monday": ["Cloud concept study", "Hands-on lab", "Architecture practice"],
                "Tuesday": ["Service deep dive", "Implementation work", "Documentation"],
                "Wednesday": ["Security focus", "Best practices", "Optimization"],
                "Thursday": ["Integration work", "Testing", "Monitoring setup"],
                "Friday": ["Mock scenarios", "Problem solving", "Review work"],
                "Saturday": ["Major project work", "Documentation", "Extra practice"],
                "Sunday": ["Weekly review", "Prepare next week", "Rest and reflect"]
            }
        }
        
        # Complete study plan with daily breakdowns
        self.study_plan = {
            "MONTH 1-2: DSA FOUNDATION": {
                "Arrays & Strings": {
                    "week_type": "DSA_WEEK",
                    "topics": {
                        "Monday": {
                            "theory": "Array implementation and basics",
                            "project": "Build dynamic array class",
                            "extra": "Time complexity analysis"
                        },
                        "Tuesday": {
                            "theory": "Two pointer patterns",
                            "project": "Implement merge sort",
                            "extra": "Space complexity optimization"
                        },
                        "Wednesday": {
                            "theory": "Sliding window technique",
                            "project": "Maximum sum subarray",
                            "extra": "Window size variations"
                        },
                        "Thursday": {
                            "theory": "Prefix sum arrays",
                            "project": "Range query implementation",
                            "extra": "2D prefix sums"
                        },
                        "Friday": {
                            "theory": "String algorithms",
                            "project": "Pattern matching",
                            "extra": "KMP algorithm"
                        }
                    }
                },
                "Hash Tables & Linked Lists": {
                    "week_type": "DSA_WEEK",
                    "topics": {
                        "Monday": {
                            "theory": "Hash function design",
                            "project": "Basic hash table",
                            "extra": "Collision handling"
                        },
                        "Tuesday": {
                            "theory": "Linked list operations",
                            "project": "Doubly linked list",
                            "extra": "Circular lists"
                        },
                        "Wednesday": {
                            "theory": "Floyd's algorithm",
                            "project": "Cycle detection",
                            "extra": "Fast/slow pointer"
                        },
                        "Thursday": {
                            "theory": "LRU cache design",
                            "project": "LRU implementation",
                            "extra": "Cache optimization"
                        },
                        "Friday": {
                            "theory": "Advanced hashing",
                            "project": "Consistent hashing",
                            "extra": "Load balancing"
                        }
                    }
                },
                "Trees & Graphs": {
                    "week_type": "DSA_WEEK",
                    "topics": {
                        "Monday": {
                            "theory": "Tree traversals",
                            "project": "Binary tree class",
                            "extra": "Iterative vs Recursive"
                        },
                        "Tuesday": {
                            "theory": "BST operations",
                            "project": "AVL tree",
                            "extra": "Tree balancing"
                        },
                        "Wednesday": {
                            "theory": "Graph representation",
                            "project": "Graph class",
                            "extra": "Edge cases"
                        },
                        "Thursday": {
                            "theory": "DFS and BFS",
                            "project": "Path finding",
                            "extra": "Optimization"
                        },
                        "Friday": {
                            "theory": "Advanced graphs",
                            "project": "Dijkstra's algorithm",
                            "extra": "Real-world applications"
                        }
                    }
                }
            },
            "MONTH 3: ADVANCED ALGORITHMS": {
                "Dynamic Programming": {
                    "week_type": "DSA_WEEK",
                    "topics": {
                        "Monday": {
                            "theory": "DP fundamentals",
                            "project": "Fibonacci with DP",
                            "extra": "Memoization"
                        },
                        "Tuesday": {
                            "theory": "1D DP patterns",
                            "project": "Climbing stairs",
                            "extra": "Space optimization"
                        },
                        "Wednesday": {
                            "theory": "2D DP",
                            "project": "Grid problems",
                            "extra": "Path counting"
                        },
                        "Thursday": {
                            "theory": "State machines",
                            "project": "Stock problems",
                            "extra": "State transitions"
                        },
                        "Friday": {
                            "theory": "String DP",
                            "project": "Edit distance",
                            "extra": "Pattern matching"
                        }
                    }
                },
                "System Design": {
                    "week_type": "SYSTEM_DESIGN_WEEK",
                    "topics": {
                        "Monday": {
                            "theory": "Design fundamentals",
                            "project": "Requirements analysis",
                            "extra": "Scale estimation"
                        },
                        "Tuesday": {
                            "theory": "Data modeling",
                            "project": "Schema design",
                            "extra": "Normalization"
                        },
                        "Wednesday": {
                            "theory": "API design",
                            "project": "REST API",
                            "extra": "GraphQL"
                        },
                        "Thursday": {
                            "theory": "System components",
                            "project": "Load balancer",
                            "extra": "Caching"
                        },
                        "Friday": {
                            "theory": "Scalability",
                            "project": "Database sharding",
                            "extra": "Replication"
                        }
                    }
                }
            },
            "MONTH 4-5: CLOUD & DEVOPS": {
                "AWS Fundamentals": {
                    "week_type": "CLOUD_WEEK",
                    "topics": {
                        "Monday": {
                            "theory": "AWS basics",
                            "project": "EC2 setup",
                            "extra": "Security groups"
                        },
                        "Tuesday": {
                            "theory": "S3 and storage",
                            "project": "Static website",
                            "extra": "Bucket policies"
                        },
                        "Wednesday": {
                            "theory": "Networking",
                            "project": "VPC setup",
                            "extra": "Subnetting"
                        },
                        "Thursday": {
                            "theory": "Databases",
                            "project": "RDS setup",
                            "extra": "Backup strategies"
                        },
                        "Friday": {
                            "theory": "Serverless",
                            "project": "Lambda function",
                            "extra": "API Gateway"
                        }
                    }
                },
                "Container Orchestration": {
                    "week_type": "CLOUD_WEEK",
                    "topics": {
                        "Monday": {
                            "theory": "Docker basics",
                            "project": "Containerization",
                            "extra": "Multi-stage builds"
                        },
                        "Tuesday": {
                            "theory": "Kubernetes concepts",
                            "project": "Pod deployment",
                            "extra": "Resource limits"
                        },
                        "Wednesday": {
                            "theory": "Services",
                            "project": "Service mesh",
                            "extra": "Ingress"
                        },
                        "Thursday": {
                            "theory": "State management",
                            "project": "Persistent volumes",
                            "extra": "StatefulSets"
                        },
                        "Friday": {
                            "theory": "Security",
                            "project": "RBAC setup",
                            "extra": "Network policies"
                        }
                    }
                }
            },
            "MONTH 6: INTERVIEW PREP": {
                "System Design Review": {
                    "week_type": "SYSTEM_DESIGN_WEEK",
                    "topics": {
                        "Monday": {
                            "theory": "Design patterns",
                            "project": "URL shortener",
                            "extra": "Rate limiting"
                        },
                        "Tuesday": {
                            "theory": "Distributed systems",
                            "project": "Chat system",
                            "extra": "Consistency"
                        },
                        "Wednesday": {
                            "theory": "Data storage",
                            "project": "Photo sharing",
                            "extra": "CDN"
                        },
                        "Thursday": {
                            "theory": "System scaling",
                            "project": "Social network",
                            "extra": "Feed generation"
                        },
                        "Friday": {
                            "theory": "Mock interviews",
                            "project": "Design review",
                            "extra": "Performance"
                        }
                    }
                },
                "Final Preparation": {
                    "week_type": "DSA_WEEK",
                    "topics": {
                        "Monday": {
                            "theory": "Algorithm review",
                            "project": "Mock interviews",
                            "extra": "Time management"
                        },
                        "Tuesday": {
                            "theory": "System design review",
                            "project": "Design questions",
                            "extra": "Trade-offs"
                        },
                        "Wednesday": {
                            "theory": "Behavioral prep",
                            "project": "Story preparation",
                            "extra": "Common questions"
                        },
                        "Thursday": {
                            "theory": "Mock interviews",
                            "project": "Feedback review",
                            "extra": "Improvements"
                        },
                        "Friday": {
                            "theory": "Final review",
                            "project": "Gap analysis",
                            "extra": "Last preparations"
                        }
                    }
                }
            }
        }

    def load_progress(self):
        """Load saved progress from file"""
        if os.path.exists('daily_progress.json'):
            with open('daily_progress.json', 'r') as f:
                self.completed = json.load(f)
        else:
            self.completed = {}

    def save_progress(self):
        """Save progress to file"""
        with open('daily_progress.json', 'w') as f:
            json.dump(self.completed, f)

    def get_week_type(self, selected_date):
        """Determine the week type based on the selected date and study plan"""
        # This is a simplified version - you might want to add more sophisticated date tracking
        for month, month_data in self.study_plan.items():
            for week, week_data in month_data.items():
                if "week_type" in week_data:
                    return week_data["week_type"]
        return "DSA_WEEK"  # Default to DSA week if no match found

    def display_tracker(self):
        """Display the study tracker interface"""
        st.title("Daily Study Plan Tracker")
        
        # Add date selector
        selected_date = st.date_input("Select Date", datetime.now())
        day_name = selected_date.strftime("%A")
        
        # Determine week type
        week_type = self.get_week_type(selected_date)
        
        # Display current focus
        st.header(f"Schedule for {day_name}")
        
        # Display daily tasks
        st.subheader("Daily Tasks")
        if day_name in self.daily_schedules[week_type]:
            for task in self.daily_schedules[week_type][day_name]:
                key = f"daily-{selected_date}-{task}"
                completed = st.checkbox(
                    task,
                    key=key,
                    value=self.completed.get(key, False)
                )
                if completed != self.completed.get(key, False):
                    self.completed[key] = completed
                    self.save_progress()
        
        # Display current topics
        st.subheader("Today's Topics")
        
        # Find matching topics for today
        for month, month_data in self.study_plan.items():
            for week, week_data in month_data.items():
                if "topics" in week_data and day_name in week_data["topics"]:
                    daily_topic = week_data["topics"][day_name]
                    
                    st.markdown(f"**Current Focus**: {month} - {week}")
                    
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.markdown("**Theory Focus:**")
                        st.write(daily_topic["theory"])
                        key = f"theory-{selected_date}"
                        completed = st.checkbox(
                            "Complete theory study",
                            key=key,
                            value=self.completed.get(key, False)
                        )
                        if completed != self.completed.get(key, False):
                            self.completed[key] = completed
                            self.save_progress()
                    
                    with col2:
                        st.markdown("**Project Work:**")
                        st.write(daily_topic["project"])
                        key = f"project-{selected_date}"
                        completed = st.checkbox(
                            "Complete project work",
                            key=key,
                            value=self.completed.get(key, False)
                        )
                        if completed != self.completed.get(key, False):
                            self.completed[key] = completed
                            self.save_progress()
                    
                    with col3:
                        st.markdown("**Extra Learning:**")
                        st.write(daily_topic["extra"])
                        key = f"extra-{selected_date}"
                        completed = st.checkbox(
                            "Complete extra learning",
                            key=key,
                            value=self.completed.get(key, False)
                        )
                        if completed != self.completed.get(key, False):
                            self.completed[key] = completed
                            self.save_progress()

def main():
    st.set_page_config(page_title="Daily Study Tracker", layout="wide")
    tracker = Study