"""
Author: [Your Name]
Date: November 26, 2025
Description: Main program to demonstrate graduation ceremony simulation
"""

from participants import Graduate, Faculty, Guest
from graduation import GraduationCeremony


def main():
    """Simulate a graduation ceremony"""
    
    # Create graduation ceremony
    ceremony = GraduationCeremony("Drexel University", "June 11, 2025")
    
    # Create one of each participant type
    print("Participants\n")
    faculty = Faculty("Dr.", "Bruce", "Banner", "Physics")
    guest = Guest("Mr.", "Brian", "Roberts", "Comcast Corporation")
    grad_student = Graduate("Radia", "Perlman", "G", "Ph.D", "Computer Science", [])
    undergrad = Graduate("Margaret", "Hamilton", "UG", "B.S.", "Mathematics", ["Cum Laude", "Medal of Freedom"])
    
    print(f"Faculty: {faculty}")
    print(f"Guest: {guest}")
    print(f"Graduate: {grad_student}")
    print(f"Undergraduate: {undergrad}")
    
    # Test announcer card
    print(f"\nAnnouncer Card for {undergrad.getFullName()}:")
    print(undergrad.getAnnouncerCard())
    
    # Add participants to ceremony
    ceremony.addSpeaker(faculty, 1)
    ceremony.addSpeaker(undergrad, 2)
    ceremony.addGraduate(grad_student)
    ceremony.addGraduate(undergrad)
    ceremony.addStagePartyMember(faculty)
    ceremony.addStagePartyMember(guest)
    print("Participants added to ceremony")
    
    # Speakers
    print("\nSpeakers")
    while ceremony.hasNextSpeaker():
        speaker = ceremony.getNextSpeaker()
        print(f"{speaker.getFullName()} speaks")
    
    # Graduates walking
    print("\nGraduates Walking")
    while ceremony.hasNextGraduate():
        graduate = ceremony.getNextGraduate()
        print(f"{graduate.getFullName()} receives diploma")
    
    # Recessional
    print("\nRecessional")
    recessional = ceremony.getRecessional()
    for name in recessional:
        print(f"{name} exits stage")
    
    # Photo manifest
    print("\nPhoto Manifest")
    current = ceremony.getPhotoManifest()
    while current is not None:
        print(f"{current.data.getFullName()}")
        current = current.next
if __name__ == "__main__":
    main()