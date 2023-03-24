### Story 1

User Story 1: As a user, I want to be able to create an account and set up a profile
Happy Path:
User clicks the “sign in/up” button on the top of the page
User uses 3rd party OAuth to sign into their account
User will input: their name, notification settings, photo
User Allows location settings to be on (so the device can recognize where the user is)

Unhappy Path:
A user tries to create an account, but along the way, something fails. The app will show an error message

Feature Significance:
	This feature is important because we want the app to keep track of useful information for each user to better enhance the user experience. This includes friends that the user studies with, total study time, and more.


User Story 3: As a user, I want to be able to notify my friends that I am studying, and invite them to come to join me
Happy Path:
	A user will click the “Study” button on the app to check-in to a study location. This will prompt the user to fill out some information about the study session. It will include:
Where the user is studying (address and room number)
How long the study session will be (end time)
Desired study subject (general studying with friends, or a focus study group for a specific subject)
Then the app will generate sharable link that can be sent to friends (optional)

Unhappy Path:
	The created study session wasn’t created, and the information isn’t stored in the database. This would show an error message to the user that their study information wasn’t able to be created.

Feature Significance:
	This feature is important because it allows the user to easily share their study information with friends and invite others to join.

User Story 4: As a user, I want to be able to view study time with friends 
Happy Path: 
Login into the app 
Go to home page to see friends 
Type in search bar or scroll to find specific friend 
Click on friend’s profile to see study time, location, and other profile data 
Unhappy Path: 
Login into the app 
Go to home page to see friends 
The user tries to find the friend 
Is unable to find the friend due to 
Mispelling their name 
Scrolling past their desired friend 
Friend not being connected to app 
User not being connect to app 

Feature Significance:
	This feature is important because it allows the user to gain information about their friend’s study situation. This also allows the app to track total studying time.

User Story 5: As a user, I want to be able to add or delete a friend from the list.
Happy Path:
Send Friend Request
search for friend’s profile
click add button
“friend request sent”
Accept/ignore Friend Request
click “pending requests”
accept/ignore the friend request
requested user is added/not added to friend list
Delete
Click on the unwanted friend’s profile
Click on the delete button
“Are you sure you want to delete this friend”
Click on “Yes” and successfully remove the friend
Unhappy Path:
You knew you added this friend and you want to delete him/her, but you cannot find his/her profile in the friend list.
Click on the delete button but it’s not working.
Error messages while deleting 
He/she still shows up in the friend list after deleting.

Feature Significance:
	This feature is important because it enables users to manage who their friends are (and who gets to see their study information) and maintain that level of privacy. At the same time, it enables users to connect with their friends to share information easily.

User Story 6: As a user, I want to send notification messages to my friends about study information (linked with Instagram messaging)

Happy Path: 
Create a study session (user story 3)
Choose Friends to notify 
Friends get notification through instagram messaging
Unhappy path:
Create a study session (user story 3) 
The user chooses who to send an invite to, the friend isn’t notified via Instagram messaging due to some sort of network failure

Feature Significance:
	This feature is important because it enables users to notify their friends whenever they create a study session and allows for personalized messaging.


