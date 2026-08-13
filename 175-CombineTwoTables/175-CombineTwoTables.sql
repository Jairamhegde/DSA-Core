-- Last updated: 8/13/2026, 8:25:20 PM
select p.firstName,p.lastName, a.city,a.state
from Person p 
left join Address a on p.personId = a.personId
