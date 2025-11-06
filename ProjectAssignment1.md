# Software Requirements and Use Cases

## Research Position Matcher
--------
Prepared by:

* `<Kevin Lai>`,`<resumemaxxers>`
* `<Ziyue Chen>`,`<resumemaxxers>`
* `<JimXiang>`,`<resumemaxxers>`
* `<Matvey Shestopalov>`,`<resumemaxxers>`

---

**Course** : CS 3733 - Software Engineering

**Instructor**: Sakire Arslan Ay

---

## Table of Contents
- [1. Introduction](#1-introduction)
- [2. Requirements Specification](#2-requirements-specification)
  - [2.1 Customer, Users, and Stakeholders](#21-customer-users-and-stakeholders)
  - [2.2 User Stories](#22-user-stories)
  - [2.3 Use Cases](#23-use-cases)
- [3. User Interface](#3-user-interface)
- [4. Product Backlog](#4-product-backlog)
- [4. References](#4-references)
- [Appendix: Grading Rubric](#appendix-grading-rubric)

<a name="revision-history"> </a>

## Document Revision History

| Name | Date       | Changes | Version |
| ------ |------------| --------- | --------- |
|Revision 1 | 2025-11-05 |Initial draft | 1.0        |
|      |            |         |         |
|      |            |         |         |

----
# 1. Introduction

Our software facilitates an easier connection between faculty and students about research opportunities and positions, particularly those not teaching undergraduate classes.  Faculty can easily reach out to students interested in their respected major. This application dissolves the barrier between students and faculty in different degree levels, and ensures qualified sophomores and juniors the opportunity to utilize their talents fully and further their academic/professional career. Students also have the opportunity to explore various research topics aligned with their interests.



----
# 2. Requirements Specification

## 2.1 Customer, Users, and Stakeholders

Customers/users include student and faculty that is part of the school organization who benefits from our software.

----
## 2.2 User Stories

1. As a student, I would like to create my student account, so that I can maintain my personal and academic information accurately in the system.
2. As a student, I want to login to the system by using my email and password or the SSO, so that I can securely access my account and manage my applications.
3. As a student, I want to view all the available research positions for me, and also see the details of the position when I click on it, so that I can explore different positions that match my interests.
4. As a student, I want to view all the recommended positions that best fit my major and interests presented in the profile, so that I can easily find research positions that best fit my profile and skills.
5. As a student, I would like to apply for a research position, so that I can submit my application and be reviewed by the faculties.
6. As a student, I want to view application status and reference updates, so that I can track the progress of my applications and stay informed about any changes or feedback made by the supervisor.
7. As a student, I want to withdraw my “pending” applications, so that I can manage my application list and avoid confusion with positions I no longer want to pursue.
8. As a student, I want to select from a predefined list of values (including date, time, etc.) so I can filter the available research opportunities and choose the most suitable one.
9. As a student, I want to view the detailed information of recommended positions, so that I can evaluate the project.
10. As a student. I want to reference a professor, so it will bolster my credibility in the application.
11. As a student, I would like to view and edit my profile information, so that I can adjust my personal and academic information in the system.


1. As a faculty, I want to activate my account so I can access the system, post research positions, and complete my profile
2. As a faculty, I want to login with username and password, so that I can access the system and post research positions
3. As a faculty, I want to view my account profile so I can have a reference and see recommendation requests
4. As a faculty, I want to create undergraduate research positions so that students can apply to different researches and solve for a real-life problem.
5. As a faculty, I want to view my list of applicants for my research position so I can figure out who I want to accept
6. As a faculty, I want to view a student applicant’s profile so I can figure out whose application I want to approve or reject
7. As a faculty, I want to approve student applications so they can be accepted into the research position
8. As a faculty, I want to reject student applications so better people can be accepted
9. As a faculty, I want to edit the predefined list of values from which user can select so they have more diversity of choice
10. As a faculty, I want to edit or delete undergraduate research positions, in case I made a mistake.
11. As a faculty, I want to be notified when a student references me in their application so I can approve or decline the reference

----
## 2.3 Use Cases

| Use case #1 |  |
|--------------|--|
| Name | View available positions |
| Participating actor | Student |
| Entry condition(s) | Student logs in to the system and enters the search page. |
| Exit condition(s) | Student selects one of the positions or navigates to another page. |
| Flow of events | 1. The student logs in to their account. 2. The student navigates to the search page. 3. The student views the available positions. 4. The student selects one position to view its details. |
| Alternative flow of events | None |
| Iteration # | 1 |

| Use case #2 |  |
|--------------|--|
| Name | View recommended positions |
| Participating actor | Student |
| Entry condition(s) | Student logs in to the system and enters the search page. |
| Exit condition(s) | Student selects one of the recommended positions or navigates to another page. |
| Flow of events | 1. The student logs in. 2. The student goes to the search page. 3. The student views the recommended positions. 4. The student selects one to view its details. |
| Alternative flow of events | None |
| Iteration # | 1 |

| Use case #3 |  |
|--------------|--|
| Name | View research position details |
| Participating actor | Student |
| Entry condition(s) | Student is logged in and viewing available or recommended positions. |
| Exit condition(s) | Student closes the position detail view. |
| Flow of events | 1. The student opens the position details page. 2. The student reviews the research position information. 3. The student exits the view. |
| Alternative flow of events | None |
| Iteration # | 1 |

| Use case #4 |  |
|--------------|--|
| Name | Apply for research position |
| Participating actor | Student |
| Entry condition(s) | Student is logged in and viewing position details. |
| Exit condition(s) | Student completes or cancels the application. |
| Flow of events | 1. The student opens the application form. 2. The student writes a short statement. 3. The student provides a faculty reference. 4. The system sends a notification to the referenced professor. 5. The student submits the application. |
| Alternative flow of events | 1. The student opens the application form. 2. The student closes the form without submitting. |
| Iteration # | 2 |

| Use case #5 |  |
|--------------|--|
| Name | View application status and reference update |
| Participating actor | Student |
| Entry condition(s) | Student is logged in and has entered the dashboard. |
| Exit condition(s) | Student leaves the dashboard or views specific application details. |
| Flow of events | 1. The student opens the dashboard. 2. The student views the current application status. 3. The student views the recommendation status after updates. |
| Alternative flow of events | None |
| Iteration # | 2 |

| Use case #6 |  |
|--------------|--|
| Name | Withdraw pending applications |
| Participating actor | Student |
| Entry condition(s) | Student is logged in, has applied to a position currently marked as pending, and is viewing the dashboard. |
| Exit condition(s) | Student withdraws the application or cancels the action. |
| Flow of events | 1. The student checks the current state of their application. 2. The student verifies that the application is in a pending state. 3. The student withdraws the application. |
| Alternative flow of events | 1. The student opens the application status page. 2. The student closes the page without taking action. |
| Iteration # | 2 |

| Use case #7 |  |
|--------------|--|
| Name | Filter research opportunities |
| Participating actor | Student |
| Entry condition(s) | Student is logged in and viewing research positions on the search page. |
| Exit condition(s) | Student closes or confirms the filters. |
| Flow of events | 1. The student clicks the filter button. 2. The student selects one or more filters. 3. The student confirms the filter selection. 4. The system updates the search results accordingly. |
| Alternative flow of events | 1. The student clicks the filter button. 2. The student selects filters. 3. The student closes the search page without confirming. |
| Iteration # | 1 |

| Use case #8 |                                                                                                                                      |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Name | Reference a professor                                                                                                                |
| Participating actor | Student                                                                                                                              |
| Entry condition(s) | Student is logged in and is in the application page.                                                                        |
| Exit condition(s) | Reference request is sent.                                                                                                           |
| Flow of events | 1. The student enters the professor’s information in the references section. 2. The system sends the reference request.                                        |
| Alternative flow of events | 1. The student enters a non-existing professor's information. 2. The system notifies the student that such professor does not exist. |
| Iteration # | 2                                                                                                                                    |


| Use case #9 |  |
|--------------|--|
| Name | View and edit student profile |
| Participating actor | Student |
| Entry condition(s) | Student is logged in. |
| Exit condition(s) | Student exits the profile and returns to the main page. |
| Flow of events | 1. The student clicks on the profile. 2. The student clicks the edit profile button. 3. The student edits profile information. 4. The student clicks the save button. 5. The system updates the profile. |
| Alternative flow of events | 1. The student clicks the edit profile button. 2. The student makes no changes. 3. The student clicks save. 4. The system displays a warning message. |
| Iteration # | 1 |

| Use case #10 |  |
|--------------|--|
| Name | View and edit faculty profile |
| Participating actor | Faculty |
| Entry condition(s) | Faculty is logged in. |
| Exit condition(s) | Faculty exits the profile and returns to the main page. |
| Flow of events | 1. The faculty clicks on the profile. 2. The faculty clicks the edit profile button. 3. The faculty edits profile details. 4. The faculty clicks save. 5. The system updates the profile. |
| Alternative flow of events | 1. The faculty clicks edit. 2. The faculty makes no changes. 3. The faculty clicks save. 4. The system displays a warning message. |
| Iteration # | 1 |

| Use case #11 |  |
|--------------|--|
| Name | Create undergraduate research position |
| Participating actor | Faculty |
| Entry condition(s) | Faculty is logged in. |
| Exit condition(s) | Research position created. |
| Flow of events | 1. The faculty opens the create research position page. 2. The faculty enters position details. 3. The faculty confirms creation. 4. The system saves the position. |
| Alternative flow of events | 1. The faculty submits incomplete details. 2. The system displays a reminder about missing fields. |
| Iteration # | 1 |

| Use case #12 |  |
|--------------|--|
| Name | Edit undergraduate research position |
| Participating actor | Faculty |
| Entry condition(s) | Faculty is logged in. |
| Exit condition(s) | Research position edited. |
| Flow of events | 1. The faculty selects a research position to edit. 2. The faculty modifies details. 3. The system saves changes. |
| Alternative flow of events | 1. The faculty selects a research position. 2. The faculty makes no modifications. |
| Iteration # | 2 |

| Use case #13 |  |
|--------------|--|
| Name | Delete undergraduate research position |
| Participating actor | Faculty |
| Entry condition(s) | Faculty is logged in and has created research positions. |
| Exit condition(s) | Research position deleted. |
| Flow of events | 1. The faculty selects a research position. 2. The faculty opens details. 3. The faculty clicks delete. 4. The faculty confirms deletion. 5. The system removes the position. |
| Alternative flow of events | 1. The faculty does not confirm deletion. 2. The system keeps the position. |
| Iteration # | 2 |

| Use case #14 |  |
|--------------|--|
| Name | View student application profiles |
| Participating actor | Faculty |
| Entry condition(s) | Faculty is logged in and viewing student applications. |
| Exit condition(s) | Faculty exits the student application profile page. |
| Flow of events | 1. The faculty navigates to the student application page. 2. The faculty views a student application profile. 3. The faculty exits the profile page. |
| Alternative flow of events | None |
| Iteration # | 2 |

| Use case #15 |  |
|--------------|--|
| Name | View student profile for faculty |
| Participating actor | Faculty |
| Entry condition(s) | Faculty is viewing student applications. |
| Exit condition(s) | Faculty exits the profile and returns to the applications list. |
| Flow of events | 1. The faculty clicks on a student profile. 2. The faculty views profile details. 3. The faculty exits the profile. |
| Alternative flow of events | None |
| Iteration # | 3 |

| Use case #16 |  |
|--------------|--|
| Name | Approve student application |
| Participating actor | Faculty |
| Entry condition(s) | Faculty is logged in and viewing student applications. |
| Exit condition(s) | Application status updated to Approved. |
| Flow of events | 1. The faculty logs in. 2. The faculty reviews a student application. 3. The faculty approves the application. 4. The system updates status to Approved. |
| Alternative flow of events | 1. The faculty reviews the application. 2. The faculty closes the page without approving. |
| Iteration # | 3 |

| Use case #17 |  |
|--------------|--|
| Name | Reject student application |
| Participating actor | Faculty |
| Entry condition(s) | Faculty is logged in and viewing student applications. |
| Exit condition(s) | Application status updated to Rejected. |
| Flow of events | 1. The faculty logs in. 2. The faculty reviews a student application. 3. The faculty rejects the application. 4. The system updates status to Rejected. |
| Alternative flow of events | 1. The faculty reviews a student application. 2. The faculty closes the page without rejecting. |
| Iteration # | 3 |

| Use case #18 |  |
|--------------|--|
| Name | Edit the predefined list of values |
| Participating actor | Faculty |
| Entry condition(s) | Faculty is logged in. |
| Exit condition(s) | Predefined list updated. |
| Flow of events | 1. The faculty enters edit mode. 2. The faculty selects a list to update. 3. The faculty updates the list. 4. The faculty confirms the update. 5. The system saves the updated list. |
| Alternative flow of events | 1. The faculty enters edit mode. 2. The faculty exits edit mode without saving. 3. No changes are made. |
| Iteration # | 3 |

| Use case #19 |  |
|--------------|--|
| Name | Edit or delete undergraduate research positions |
| Participating actor | Faculty |
| Entry condition(s) | Faculty is logged in and viewing existing research positions. |
| Exit condition(s) | Position edited, deleted, or unchanged. |
| Flow of events | 1. The faculty views research positions. 2. The faculty chooses to edit or delete a position. 3. The faculty saves or confirms changes. 4. The system updates records. |
| Alternative flow of events | 1. The faculty makes no changes. 2. The faculty exits without saving. |
| Iteration # | 3 |

| Use case #20 |  |
|--------------|--|
| Name | Approve or decline student reference request |
| Participating actor | Faculty |
| Entry condition(s) | Faculty is logged in and viewing notifications. |
| Exit condition(s) | Reference status updated. |
| Flow of events | 1. The faculty opens notifications. 2. The faculty reviews a reference request. 3. The faculty approves or declines. 4. The system updates the reference status. |
| Alternative flow of events | 1. The faculty opens notifications. 2. The faculty closes the page without responding. |
| Iteration # | 3 |

| Use case #21 |                                                                                                 |
|--------------|-------------------------------------------------------------------------------------------------|
| Name | Receive student reference notification                                                          |
| Participating actor | Faculty                                                                                         |
| Entry condition(s) | Faculty is logged in.                                                                           |
| Exit condition(s) | Notification received.                                                                          |
| Flow of events | 1. The student confirms a reference request. 2. The system sends a notification to the faculty. |
| Alternative flow of events | 1. The student provides a non-existing professor's email/name. 2. A warning is displayed.       |
| Iteration # | 3                                                                                               |


----
# 3. User Interface

<kbd>Applications and references (student): <img src ="md-images/apps_refs.png"></img></kbd>

<kbd>My positions (faculty): <img src ="md-images/my_positions.png"></img></kbd>

<kbd>Login page (all): <img src ="md-images/login_page.png"></img></kbd>

<kbd>Application page (student): <img src ="md-images/application_page.png"></img></kbd>

<kbd>Edit or create position (faculty): <img src ="md-images/edit_or_create.png"></img></kbd>

<kbd>Edit student profile (student): <img src ="md-images/student_profile_edit.png"></img></kbd>

<kbd>View student profile (faculty): <img src ="md-images/view_student_profile.png"></img></kbd>

<kbd>Inbox (faculty): <img src ="md-images/inbox.png"></img></kbd>

<kbd>Open positions (student): <img src ="md-images/open_positions.png"></img></kbd>

<kbd>Position details (all): <img src ="md-images/position_details.png"></img></kbd>

<kbd>Applications for a position (faculty): <img src ="md-images/apps_for_position.png"></img></kbd>

----
# 4. Product Backlog

https://github.com/WPI-CS3733-2025B/team-resumemaxxers/issues

----
# 5. References
