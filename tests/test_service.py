import sys
from pathlib import Path 

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))

from taskcli.service import TaskService

def test_add_task():
    service = TaskService()
    task = service.add_task("Test Task 13")
    assert task.title == "Test Task 13"
    assert not task.done

def test_list_tasks():
    service = TaskService()
    service.add_task("Task 15")
    service.add_task("Task 16")
    
    tasks = service.list_tasks()
    
    assert len(tasks) >= 2
    assert any(task.title == "Task 15" for task in tasks)
    assert any(task.title == "Task 16" for task in tasks)

def test_remove_task():
    service = TaskService()
    task = service.add_task("Task to Remove 4")
    
    assert service.remove_task(task.id) == True
    #assert service.remove_task("non-existent-id") == False

def test_complete_task():
    service = TaskService()
    task = service.add_task("Task to Complete 5")

    assert service.complete_task(task.id) == True
    #assert service.complete_task("non-existent-id") == False