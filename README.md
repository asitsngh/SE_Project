# Automation of equipment collection

## Contribution:
I welcome any and all contributions! Here are some ways you can get started:

- Report bugs: If you encounter any bugs, please let us know. Open up an issue and let us know the problem.
- Contribute code: If you are a developer and want to contribute, follow the instructions below to get started!
- Suggestions: If you don't want to code but have some awesome ideas, open up an issue explaining some updates or imporvements you would like to see!
- Documentation: If you see the need for some additional documentation, feel free to add some!

## Problem Statement: 
The goal of this project is to automate the equipment collection process for the PE department of the college. Currently, the process involves students manually recording their equipment borrowing and return details in a register or notebook.  They must also leave their ID cards as a kind of a mortgage which is only returned upon the return of the equipment. However, this system is out dated, cumbersome, and challenging to maintain.

## Proposed solution:
To address the issues discussed previously, we propose implementing an upgraded system. In the new system, students will use their ID cards to simplify the equipment collection process. They will enter their names and register number, which will then be entered into two Excel sheets. When students return the equipment, they will enter their register numbers again, removing their names from one sheet and recording the return time on the other. This approach allows one sheet to track unreturned items, while the other sheet maintains the complete history of equipment transactions.

## Advantages:
This automated system offers several advantages. It eliminates the requirement for students to surrender their ID cards as collateral, making the process more convenient. Furthermore, it streamlines the equipment collection process for the PE department, simplifying management and maintenance of equipment records. The two Excel sheets provide clear visibility into borrowed equipment and create a comprehensive history log, enhancing accountability and facilitating usage analysis. By automating the equipment collection process through the use of a biometric device, students' ID cards, and Excel sheets, your project aims to modernize and improve the management of equipment transactions within the PE department. This improvement will benefit both students and staff by streamlining the process and eliminating the need for ID card collateral.

## System Requirements Specification:
The device running this application needs to have python and MS Excel pre-installed.

## Conclusion and Future work:
This project aims to streamline the process of maintaining and retrieving records of unrecovered equipment. Although the current implementation is simple, its simplicity allows for future modifications and enhancements. One potential improvement is to optimize the user input process. Instead of requiring students to manually enter both their names and register numbers, we can leverage the existing database accessible to the college authority to automatically retrieve additional details such as email IDs, hostel block, room numbers, and mobile numbers based on the provided register number. Another enhancement could involve implementing a more convenient and hands-free method for capturing student information, such as utilizing an ID card scanner to extract all the required details from the student's ID card. These enhancements would not only improve the user experience but also increase efficiency and accuracy in maintaining and managing equipment records. 

