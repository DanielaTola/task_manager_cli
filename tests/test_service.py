import sys
from pathlib import Path 

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))

from taskcli.service import TaskService

def test_add_task():
    service = TaskService()
    task = service.add_task("Test Task 3")
    assert task.title == "Test Task 3"
    assert not task.done

def test_list_tasks():
    service = TaskService()
    service.add_task("Task 5")
    service.add_task("Task 6")
    
    tasks = service.list_tasks()
    
    assert len(tasks) >= 2
    assert any(task.title == "Task 5" for task in tasks)
    assert any(task.title == "Task 6" for task in tasks)

def test_remove_task():
    service = TaskService()
    task = service.add_task("Task to Remove")
    
    assert service.remove_task(task.id) == True
    assert service.remove_task("non-existent-id") == False

# def test_complete_task():
#     service = TaskService()
#     task = service.add_task("Task to Complete")

#     assert service.complete_task(task.id) == True
#     assert service.complete_task("non-existent-id") == False