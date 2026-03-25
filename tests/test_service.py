from taskcli.service import TaskService

def test_add_task():
    service = TaskService()
    task = service.add_task("Test Task 13")
    assert task.title == "Test Task 13"
    assert  task.done is False

def test_list_tasks():
    service = TaskService()
    service.add_task("Task 15")
    service.add_task("Task 16")
    
    tasks = service.list_tasks()
    
    assert len(tasks) > 0 
    #assert any(task.title == "Task 15" for task in tasks)
    #assert any(task.title == "Task 16" for task in tasks)

def test_remove_task():
    service = TaskService()
    task = service.add_task("Task to Remove 4")
    
    assert service.remove_task(task.id)
    assert not service.remove_task("non-existent-id")

def test_complete_task():
    service = TaskService()
    task = service.add_task("Task to Complete 5")

    assert service.complete_task(task.id)
    assert not service.complete_task("non-existent-id") 
    