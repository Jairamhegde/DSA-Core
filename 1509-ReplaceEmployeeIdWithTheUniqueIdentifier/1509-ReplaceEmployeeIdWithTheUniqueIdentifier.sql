-- Last updated: 8/13/2026, 8:21:41 PM
select b.unique_id,a.name
from Employees as a
left join EmployeeUNI as b
on a.id=b.id
