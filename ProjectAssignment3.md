# Project Design Document

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
- [2. Software Design](#2-software-design)
    - [2.1 Database Model](#21-model)
    - [2.2 Modules and Interfaces](#22-modules-and-interfaces)
    - [2.2.1 Overview](#221-overview)
    - [2.2.2 Interfaces](#222-interfaces)
    - [2.3 User Interface Design](#23-view-and-user-interface-design)
- [3. References](#3-references)
- [Appendix: Grading Rubric](#appendix-grading-rubric)

<a name="revision-history"> </a>

### Document Revision History

| Name | Date       | Changes | Version |
| ------ |------------| --------- | --------- |
|Revision 1 | 2025-11-11 |Initial draft | 1.0        |
|      |            |         |         |


# 1. Introduction

The purpose of this document is to describe the design of the Research Position Matcher app.

# 2. Software Design

## 2.1 Database Model

Class Tables

### Class Tables

*   **Student**: Represents a student user in the system. It stores their profile information, including GPA, and links to their applications, majors, research interests, courses, and applications.
    ```sql
    CREATE TABLE student (
        id INTEGER NOT NULL,
        username VARCHAR(64) NOT NULL,
        firstname VARCHAR(64) NOT NULL,
        lastname VARCHAR(64) NOT NULL,
        email VARCHAR(120) NOT NULL,
        password_hash VARCHAR(256),
        gpa FLOAT,
        PRIMARY KEY (id),
        UNIQUE (username),
        UNIQUE (email)
    );
    ```

*   **Faculty**: Represents a faculty member user. It links to the research positions they have created and the recommendations they have been asked to provide.
    ```sql
    CREATE TABLE faculty (
        id INTEGER NOT NULL,
        username VARCHAR(64) NOT NULL,
        firstname VARCHAR(64) NOT NULL,
        lastname VARCHAR(64) NOT NULL,
        email VARCHAR(120) NOT NULL,
        password_hash VARCHAR(256),
        PRIMARY KEY (id),
        UNIQUE (username),
        UNIQUE (email)
    );
    ```

*   **Position**: Represents a research position created by a faculty member. It contains all the details about the position, including description, requirements, and start/end dates.
    ```sql
    CREATE TABLE position (
        id INTEGER NOT NULL,
        name VARCHAR(100) NOT NULL,
        description VARCHAR(512),
        start_date DATETIME,
        end_date DATETIME,
        team_size INTEGER NOT NULL,
        min_gpa FLOAT,
        faculty_id INTEGER NOT NULL,
        ref_required BOOLEAN NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(faculty_id) REFERENCES faculty (id)
    );
    ```

*   **Application**: Represents a student's application to a specific research Position. It stores the student's statement and the status of the application (e.g., pending, accepted, rejected).
    ```sql
    CREATE TABLE application (
        id INTEGER NOT NULL,
        student_id INTEGER NOT NULL,
        position_id INTEGER NOT NULL,
        statement VARCHAR(1500),
        status VARCHAR(64) NOT NULL,
        created_at DATETIME NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(student_id) REFERENCES student (id),
        FOREIGN KEY(position_id) REFERENCES position (id)
    );
    ```

*   **Major**: A simple table that stores the names of academic majors. It is used to associate students and positions with specific majors.
    ```sql
    CREATE TABLE major (
        id INTEGER NOT NULL,
        name VARCHAR(100) NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (name)
    );
    ```

*   **Course**: Stores information about individual courses, including their name and number. It is linked to a Major.
    ```sql
    CREATE TABLE course (
        id INTEGER NOT NULL,
        name VARCHAR(100) NOT NULL,
        coursenum VARCHAR(10) NOT NULL,
        major_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(major_id) REFERENCES major (id)
    );
    ```

*   **Recommendation**: Tracks a request from a Student to a Faculty member for a recommendation. It holds the status of the request.
    ```sql
    CREATE TABLE recommendation (
        id INTEGER NOT NULL,
        student_id INTEGER NOT NULL,
        faculty_id INTEGER NOT NULL,
        status VARCHAR(64) NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(student_id) REFERENCES student (id),
        FOREIGN KEY(faculty_id) REFERENCES faculty (id)
    );
    ```

*   **ResearchTopic**: A table to store different research topics. This allows for connecting students' interests and position requirements.
    ```sql
    CREATE TABLE research_topic (
        name VARCHAR(100) NOT NULL,
        PRIMARY KEY (name)
    );
    ```

*   **Language**: A table to store different languages.
    ```sql
    CREATE TABLE language (
        name VARCHAR(100) NOT NULL,
        PRIMARY KEY (name)
    );
    ```

### Association Tables

*   **students_majors**: Links students with their respective majors.
    ```sql
    CREATE TABLE students_majors (
        student_id INTEGER NOT NULL,
        major_id INTEGER NOT NULL,
        PRIMARY KEY (student_id, major_id),
        FOREIGN KEY(student_id) REFERENCES student (id),
        FOREIGN KEY(major_id) REFERENCES major (id)
    );
    ```

*   **students_research_topics**: Links students with their research interests.
    ```sql
    CREATE TABLE students_research_topics (
        student_id INTEGER NOT NULL,
        research_topic_name VARCHAR NOT NULL,
        PRIMARY KEY (student_id, research_topic_name),
        FOREIGN KEY(student_id) REFERENCES student (id),
        FOREIGN KEY(research_topic_name) REFERENCES research_topic (name)
    );
    ```

*   **students_languages**: Links students with the languages they know.
    ```sql
    CREATE TABLE students_languages (
        student_id INTEGER NOT NULL,
        language_name VARCHAR NOT NULL,
        PRIMARY KEY (student_id, language_name),
        FOREIGN KEY(student_id) REFERENCES student (id),
        FOREIGN KEY(language_name) REFERENCES language (name)
    );
    ```

*   **positions_majors**: Links research positions with required academic majors.
    ```sql
    CREATE TABLE positions_majors (
        position_id INTEGER NOT NULL,
        major_id INTEGER NOT NULL,
        PRIMARY KEY (position_id, major_id),
        FOREIGN KEY(position_id) REFERENCES position (id),
        FOREIGN KEY(major_id) REFERENCES major (id)
    );
    ```

*   **positions_research_topics**: Links research positions with relevant research topics.
    ```sql
    CREATE TABLE positions_research_topics (
        position_id INTEGER NOT NULL,
        research_topic_name VARCHAR NOT NULL,
        PRIMARY KEY (position_id, research_topic_name),
        FOREIGN KEY(position_id) REFERENCES position (id),
        FOREIGN KEY(research_topic_name) REFERENCES research_topic (name)
    );
    ```

*   **positions_languages**: Links research positions with required languages.
    ```sql
    CREATE TABLE positions_languages (
        position_id INTEGER NOT NULL,
        language_name VARCHAR NOT NULL,
        PRIMARY KEY (position_id, language_name),
        FOREIGN KEY(position_id) REFERENCES position (id),
        FOREIGN KEY(language_name) REFERENCES language (name)
    );
    ```

*   **positions_courses**: Links research positions with recommended or required courses.
    ```sql
    CREATE TABLE positions_courses (
        position_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        PRIMARY KEY (position_id, course_id),
        FOREIGN KEY(position_id) REFERENCES position (id),
        FOREIGN KEY(course_id) REFERENCES course (id)
    );
    ```

*   **course_enrollment**: Links students to the courses they are enrolled in and stores their grade.
    ```sql
    CREATE TABLE course_enrollment (
        id INTEGER NOT NULL,
        student_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        grade VARCHAR(2),
        PRIMARY KEY (id),
        FOREIGN KEY(student_id) REFERENCES student (id),
        FOREIGN KEY(course_id) REFERENCES course (id)
    );
    ```
    
Provide a UML diagram of your database model showing the associations and relationships among tables. 

## 2.2 Modules and Interfaces

### 2.2.1 Overview
Describe the high-level architecture of your software:  i.e., the major modules/blueprints and how they fit together. Provide a UML component diagram that illustrates the architecture of your software. Briefly mention the role of each module in your architectural design. Please refer to the "System Level Design" lectures in Week 4. 

### 2.2.2 Interfaces

Include a detailed description of the routes your application will implement. 
* Brainstorm with your team members and identify all routes you need to implement for the **completed** application.
* For each route specify its “methods”, “URL path”, and “a description of the operation it implements”.  
* You can use the following table template to list your route specifications. 
* Organize this section according to your module decomposition, i.e., include a sub-section for each module/blueprint and list all routes for that sub-section in a table.  

#### 2.2.2.1 \<Blueprint1> Routes

|   | Methods           | URL Path   | Description  |
|:--|:------------------|:-----------|:-------------|
|1. |                   |            |              |
|2. |                   |            |              |
|3. |                   |            |              |
|4. |                   |            |              |
|5. |                   |            |              |
|6. |                   |            |              |

#### 2.2.2.2 \<Blueprint2> Routes

|   | Methods           | URL Path   | Description  |
|:--|:------------------|:-----------|:-------------|
|1. |                   |            |              |
|2. |                   |            |              |
|3. |                   |            |              |
|4. |                   |            |              |
|5. |                   |            |              |
|6. |                   |            |              |

Repeat the above for other modules you included in your application. 

### 2.3 User Interface Design 

Provide UI sketches or screenshots for the following pages:
 * Faculty main page
 * Student main page (show how you will display "all positions" vs "recommended positions")
 * Faculty creating a position 
 * Faculty accepting /rejecting an application
 * Student applying a position

# 3. References

Cite your references here.

For the papers you cite give the authors, the title of the article, the journal name, journal volume number, date of publication and inclusive page numbers. Giving only the URL for the journal is not appropriate.

For the websites, give the title, author (if applicable) and the website URL.

----
# Appendix: Grading Rubric
(Please remove this part in your final submission)

 * You will first  submit a draft version of this document:
    * "Project 3 : Project Design Document - draft" (5pts). 
* We will provide feedback on your document and you will revise and update it.
    * "Project 5 : Project Design Document - final" (80pts) 

Below is the grading rubric that we will use to evaluate the final version of your document. 

|**MaxPoints**| **Design** |
|:---------:|:-------------------------------------------------------------------------|
|           | Are all parts of the document in agreement with the product requirements? |
| TBA         | Is the architecture of the system ([2.2.1 Overview](#221-overview)) described well, with the major components and their interfaces?         
| TBA        | Is the database model (i.e., [2.1 Database Model](#21-database-model)) explained well with sufficient detail? Do the team clearly explain the purpose of each table included in the model?| 
|          | Is the document making good use of semi-formal notation (i.e., UML diagrams)? Does the document provide a clear UML class diagram visualizing the DB model of the system? |
| TBA        | Is the UML class diagram complete? Does it include all classes (tables) and does it clearly mark the PK and FKs for each table? Does it clearly show the associations between them? Are the multiplicities of the associations shown correctly? ([2.1 Database Model](#21-database-model)) |
| TBA        | Are all major interfaces (i.e., the routes) listed? Are the routes explained in sufficient detail? ([2.2.2 Interfaces](#222-interfaces)) |
| TBA        | Is the view and the user interfaces explained well? Did the team provide the screenshots of the interfaces they built so far.  ([2.3 User Interface Design](#23-user-interface-design)) |
|           | **Clarity** |
|           | Is the solution at a fairly consistent and appropriate level of detail? Is the solution clear enough to be turned over to an independent group for implementation and still be understood? |
| TBA         | Is the document carefully written, without typos and grammatical errors?  |
| TBA         | Is the document well formatted? (Make sure to check your document on GitHub. You will loose points if there are formatting issues in your document.  )  |
|           |  |
|          | **Total** |
|           |  |