from src.taskcli.service import TaskService

def test_add_task():
    service = TaskService()
    task = service.add_task("Test Task")
    
    assert task.title == "Test Task"
    assert not task.done

def test_list_tasks():
    service = TaskService()
    service.add_task("Task 1")
    service.add_task("Task 2")
    
    tasks = service.list_tasks()
    
    assert len(tasks) >= 2
    assert any(task.title == "Task 1" for task in tasks)
    assert any(task.title == "Task 2" for task in tasks)

def test_remove_task():
    service = TaskService()
    task = service.add_task("Task to Remove")
    
    assert service.remove_task(task.id) == True
    assert service.remove_task("non-existent-id") == False

def test_complete_task():
    service = TaskService()
    task = service.add_task("Task to Complete")

    assert service.complete_task(task.id) == True
    assert service.complete_task("non-existent-id") == False