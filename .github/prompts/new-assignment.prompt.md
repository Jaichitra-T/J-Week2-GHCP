---
agent: agent
description: Create a new programming homework assignment
argument-hint: Provide assignment details
---

# New Assignment Prompt

You are helping to create a new homework assignment for a computer science course. Follow these guidelines when generating assignment content:

## Assignment Requirements

1. **Follow the Template Structure**
   - Use the structure defined in `templates/assignment-template.md`
   - Create a `README.md` file in a new subdirectory under `assignments/`
   - Include folder name in snake_case (e.g., `python-basics`, `games-in-python`)

2. **Content Standards**
   - **Learning-focused**: Design with clear learning objectives and appropriate difficulty levels for the course
   - **Student-friendly**: Use clear, encouraging language that motivates students
   - **Actionable**: Provide specific, measurable tasks with clear requirements

3. **Structure Elements**
   - **Title** (📘): Short, descriptive assignment name
   - **Objective** (🎯): 1-2 sentences on what students will learn/accomplish
   - **Tasks** (📝): One or more tasks with:
     - Task title (🛠️)
     - Description: Clear instruction of what needs to be done
     - Requirements: Specific, measurable outcomes as bullet points

4. **Metadata**
   - Include `applyTo` field specifying applicable cohorts/groups
   - Example: `applyTo: ["cohort-1", "cohort-2"]`

5. **Supporting Files**
   - Include starter code (`starter-code.py`, etc.) when appropriate
   - Include sample data files (`.csv`, `.json`, etc.) if needed
   - Add any supporting documentation as needed

## Example Output

When creating an assignment, structure it exactly as shown in the template with proper markdown formatting and emoji usage.

---

# Create New Programming Assignment

Your goal is to generate a new homework assignment for the Mergington High School students.

## Step 1: Gather Assignment Information

If not already provided by the user, ask what the assignment will be about.

## Step 2: Create Assignment Structure

1. Create a new directory in the `assignments` folder with a unique name based on the assignment topic
1. Create a new file in the directory named `README.md` with the structure from the [assignment-template.md](../../templates/assignment-template.md) file
1. Fill out the assignment details in the README file
1. (Optional) Add starter code or attachments if the assignment needs them - add these files to the same assignment folder

## Step 3: Update Website Configuration

Update the assignments list in [config.json](../../config.json) website configuration file to include the new assignment. For the dueDate field, use the current date plus 7 days unless specified otherwise.
