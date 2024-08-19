import pygame
import pyttsx3
import speech_recognition as sr

# Initialize Pygame
pygame.init()

# Initialize pyttsx3 for speech synthesis
engine = pyttsx3.init()

def speak(text):
    global current_text
    current_text = text
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Could you repeat?")
        return recognize_speech()
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

def main():
    # Set up the window
    window_width = 800
    window_height = 600
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Talking Human')

    # Load human images for different mouth states
    human_images = {
        'closed': pygame.image.load('avatar_closed.png'),
        'half_open': pygame.image.load('avatar_half_open.png'),
        'open': pygame.image.load('avatar_open.png')
    }
    current_mouth_state = 'closed'  # Start with the mouth closed

    human_rect = human_images['closed'].get_rect()
    human_rect.center = (window_width // 2, window_height // 2)

    speak("Hello! Ask me about Sevendyne IT consultancy")

    pygame.time.wait(1000)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Example for cycling through mouth states
        if current_mouth_state == 'closed':
            current_mouth_state = 'half_open'
        elif current_mouth_state == 'half_open':
            current_mouth_state = 'open'
        else:
            current_mouth_state = 'closed'
        
        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw the current mouth state
        screen.blit(human_images[current_mouth_state], human_rect)

        # Update the display
        pygame.display.flip()

        clock.tick(10)

        # Check if speech recognition has finished
        response = recognize_speech()
        if "what services does they offer" in response.lower():
            speak("Sevendyne offers HR staffing, technical training and app development ")
        elif "what product are they currently developing" in response.lower():
            speak("Sevendyne is developing HRMS (Human Resource Management System) software.")
        elif "can they assist with custom app development" in response.lower():
            speak("Yes, Sevendyne specializes in custom app development. ")
        elif "thank you" in response.lower():
            speak("You are welcome. ")
        else:
            speak("Are you interested in collaborating with Sevendyne IT Consultancy")

        pygame.time.wait(1000)

    pygame.quit()

if __name__ == "__main__":
    main()
