with recursive alltasks as (
select task_id,subtasks_count  as subtask_id
from tasks
union all
select task_id,subtask_id-1
from alltasks
where subtask_id>1
)
select t.task_id,t.subtask_id from
alltasks t
left join executed e
on e.task_id=t.task_id and e.subtask_id=t.subtask_id
where e.subtask_id is  null