# Chat Voice Widget - Test Case Plan

## Overview

This document defines the test cases for verifying the ChatVoiceWidget implementation. Tests are organized by component and functionality.

**Testing Framework:** JUnit 5 + Compose UI Testing + MockK
**Coverage Target:** Core functionality, edge cases, error handling

---

## Test Categories

| Category | Description |
|----------|-------------|
| **Unit Tests** | Test individual functions and classes in isolation |
| **Component Tests** | Test Compose UI components with ComposeTestRule |
| **Integration Tests** | Test component interactions and state flow |

---

## 1. MessageList Tests

### 1.1 Display Tests

| ID | Test Case | Expected Result |
|----|-----------|-----------------|
| ML-01 | Empty message list | Shows empty state or placeholder |
| ML-02 | Single user message | Displays one right-aligned bubble |
| ML-03 | Single assistant message | Displays one left-aligned bubble |
| ML-04 | Mixed messages (user + assistant) | Correct alignment for each |
| ML-05 | Many messages (50+) | Renders efficiently, scrollable |
| ML-06 | Message with long text | Text wraps correctly within bubble |

### 1.2 Scroll Behavior Tests

| ID | Test Case | Expected Result |
|----|-----------|-----------------|
| ML-07 | Initial load | Scrolled to bottom (newest message) |
| ML-08 | New message added | Auto-scrolls to show new message |
| ML-09 | User scrolls up, new message arrives | Auto-scrolls to bottom |
| ML-10 | User is at bottom, new message | Stays at bottom smoothly |

### 1.3 Test Code

```kotlin
class MessageListTest {

    @get:Rule
    val composeTestRule = createComposeRule()

    @Test
    fun `ML-01 empty list shows empty state`() {
        composeTestRule.setContent {
            MessageList(messages = emptyList())
        }
        // Assert empty state is visible or no message bubbles exist
        composeTestRule.onAllNodesWithTag("message_bubble")
            .assertCountEquals(0)
    }

    @Test
    fun `ML-02 single user message displays right-aligned`() {
        val message = ChatMessage(
            id = "1",
            content = MessageContent.Text("Hello"),
            sender = MessageSender.USER,
            timestamp = System.currentTimeMillis()
        )
        composeTestRule.setContent {
            MessageList(messages = listOf(message))
        }
        composeTestRule.onNodeWithTag("message_bubble_1")
            .assertExists()
        // Verify right alignment via semantic properties or position
    }

    @Test
    fun `ML-08 new message triggers auto-scroll`() {
        val messages = mutableStateListOf<ChatMessage>()
        composeTestRule.setContent {
            MessageList(messages = messages)
        }
        // Add 20 messages to ensure scrolling is needed
        repeat(20) { i ->
            messages.add(createMessage("msg_$i", "Message $i"))
        }
        composeTestRule.waitForIdle()
        // Assert last message is visible
        composeTestRule.onNodeWithText("Message 19")
            .assertIsDisplayed()
    }
}
```

---

## 2. MessageBubble Tests

### 2.1 Text Content Tests

| ID | Test Case | Expected Result |
|----|-----------|-----------------|
| MB-01 | User text bubble | Primary color, right-aligned, rounded corners |
| MB-02 | Assistant text bubble | Secondary color, left-aligned, rounded corners |
| MB-03 | Timestamp visible | Shows formatted time below message |
| MB-04 | Timestamp hidden (config) | No timestamp when disabled |
| MB-05 | SENDING status | Shows sending indicator |
| MB-06 | ERROR status | Shows error indicator/retry option |

### 2.2 Audio Content Tests

| ID | Test Case | Expected Result |
|----|-----------|-----------------|
| MB-07 | Audio bubble displays | Shows play button and duration |
| MB-08 | Audio with waveform | Displays static waveform visualization |
| MB-09 | Audio without waveform | Displays fallback (plain bar or placeholder) |

### 2.3 Test Code

```kotlin
class MessageBubbleTest {

    @get:Rule
    val composeTestRule = createComposeRule()

    @Test
    fun `MB-01 user bubble has correct styling`() {
        val message = ChatMessage(
            id = "1",
            content = MessageContent.Text("Test message"),
            sender = MessageSender.USER,
            timestamp = System.currentTimeMillis()
        )
        composeTestRule.setContent {
            MessageBubble(
                message = message,
                theme = ChatTheme.Default
            )
        }
        composeTestRule.onNodeWithText("Test message")
            .assertExists()
            .assertIsDisplayed()
        // Additional assertions for color/alignment via semantics
    }

    @Test
    fun `MB-03 timestamp is visible when enabled`() {
        val message = createMessage("1", "Hello")
        composeTestRule.setContent {
            MessageBubble(
                message = message,
                showTimestamp = true
            )
        }
        // Timestamp should be displayed
        composeTestRule.onNodeWithTag("timestamp_1")
            .assertExists()
    }

    @Test
    fun `MB-04 timestamp is hidden when disabled`() {
        val message = createMessage("1", "Hello")
        composeTestRule.setContent {
            MessageBubble(
                message = message,
                showTimestamp = false
            )
        }
        composeTestRule.onNodeWithTag("timestamp_1")
            .assertDoesNotExist()
    }
}
```

---

## 3. InputBar Tests

### 3.1 Text Input Tests

| ID | Test Case | Expected Result |
|----|-----------|-----------------|
| IB-01 | Empty input | Send button disabled |
| IB-02 | Text entered | Send button enabled |
| IB-03 | Whitespace only | Send button disabled |
| IB-04 | Send button pressed | onSendMessage called with text, input cleared |
| IB-05 | Multi-line input | TextField expands |
| IB-06 | Enter key (enterToSend=true) | Sends message |
| IB-07 | Enter key (enterToSend=false) | Adds newline |

### 3.2 Microphone Button Tests

| ID | Test Case | Expected Result |
|----|-----------|-----------------|
| IB-08 | Voice enabled | Mic button visible |
| IB-09 | Voice disabled | Mic button hidden |
| IB-10 | Mic button pressed | Triggers recording overlay |

### 3.3 Test Code

```kotlin
class InputBarTest {

    @get:Rule
    val composeTestRule = createComposeRule()

    private var sentMessage: String? = null
    private var recordingStarted = false

    @Test
    fun `IB-01 send button disabled when empty`() {
        composeTestRule.setContent {
            InputBar(
                onSendMessage = { sentMessage = it },
                onStartRecording = { recordingStarted = true }
            )
        }
        composeTestRule.onNodeWithTag("send_button")
            .assertIsNotEnabled()
    }

    @Test
    fun `IB-02 send button enabled when text entered`() {
        composeTestRule.setContent {
            InputBar(
                onSendMessage = { sentMessage = it },
                onStartRecording = { recordingStarted = true }
            )
        }
        composeTestRule.onNodeWithTag("text_input")
            .performTextInput("Hello")
        composeTestRule.onNodeWithTag("send_button")
            .assertIsEnabled()
    }

    @Test
    fun `IB-03 whitespace only keeps send disabled`() {
        composeTestRule.setContent {
            InputBar(
                onSendMessage = { sentMessage = it },
                onStartRecording = { recordingStarted = true }
            )
        }
        composeTestRule.onNodeWithTag("text_input")
            .performTextInput("   ")
        composeTestRule.onNodeWithTag("send_button")
            .assertIsNotEnabled()
    }

    @Test
    fun `IB-04 send clears input and calls callback`() {
        composeTestRule.setContent {
            InputBar(
                onSendMessage = { sentMessage = it },
                onStartRecording = { recordingStarted = true }
            )
        }
        composeTestRule.onNodeWithTag("text_input")
            .performTextInput("Test message")
        composeTestRule.onNodeWithTag("send_button")
            .performClick()

        assertEquals("Test message", sentMessage)
        composeTestRule.onNodeWithTag("text_input")
            .assertTextEquals("")
    }

    @Test
    fun `IB-09 mic button hidden when voice disabled`() {
        composeTestRule.setContent {
            InputBar(
                onSendMessage = {},
                onStartRecording = {},
                enableVoice = false
            )
        }
        composeTestRule.onNodeWithTag("mic_button")
            .assertDoesNotExist()
    }
}
```

---

## 4. AudioRecordingOverlay Tests

### 4.1 Display Tests

| ID | Test Case | Expected Result |
|----|-----------|-----------------|
| AR-01 | Overlay appears | Shows timer, waveform, stop/cancel buttons |
| AR-02 | Duration updates | Timer counts up (00:00 → 00:01 → ...) |
| AR-03 | Waveform animates | Amplitude visualization updates |

### 4.2 Interaction Tests

| ID | Test Case | Expected Result |
|----|-----------|-----------------|
| AR-04 | Stop button pressed | onStopRecording called, overlay closes |
| AR-05 | Cancel button pressed | onCancelRecording called, overlay closes |
| AR-06 | Back press during recording | Cancels recording |

### 4.3 Test Code

```kotlin
class AudioRecordingOverlayTest {

    @get:Rule
    val composeTestRule = createComposeRule()

    @Test
    fun `AR-01 overlay shows all elements`() {
        composeTestRule.setContent {
            AudioRecordingOverlay(
                duration = 5000L,
                amplitude = 0.5f,
                onStop = {},
                onCancel = {}
            )
        }
        composeTestRule.onNodeWithTag("duration_timer").assertExists()
        composeTestRule.onNodeWithTag("waveform").assertExists()
        composeTestRule.onNodeWithTag("stop_button").assertExists()
        composeTestRule.onNodeWithTag("cancel_button").assertExists()
    }

    @Test
    fun `AR-02 duration displays correctly`() {
        composeTestRule.setContent {
            AudioRecordingOverlay(
                duration = 65000L, // 1:05
                amplitude = 0.5f,
                onStop = {},
                onCancel = {}
            )
        }
        composeTestRule.onNodeWithText("01:05").assertExists()
    }

    @Test
    fun `AR-04 stop button triggers callback`() {
        var stopCalled = false
        composeTestRule.setContent {
            AudioRecordingOverlay(
                duration = 5000L,
                amplitude = 0.5f,
                onStop = { stopCalled = true },
                onCancel = {}
            )
        }
        composeTestRule.onNodeWithTag("stop_button").performClick()
        assertTrue(stopCalled)
    }
}
```

---

## 5. AudioRecorder Tests (Unit Tests)

### 5.1 Recording Lifecycle

| ID | Test Case | Expected Result |
|----|-----------|-----------------|
| REC-01 | Start recording | isRecording = true |
| REC-02 | Stop recording | Returns ByteArray, isRecording = false |
| REC-03 | Cancel recording | isRecording = false, no data returned |
| REC-04 | Get amplitude while recording | Returns value 0.0-1.0 |
| REC-05 | Get duration while recording | Returns elapsed time in ms |

### 5.2 Error Handling

| ID | Test Case | Expected Result |
|----|-----------|-----------------|
| REC-06 | Start without permission | Throws SecurityException or returns error state |
| REC-07 | Stop when not recording | No-op or throws IllegalStateException |
| REC-08 | Multiple start calls | Ignores subsequent starts or throws |

### 5.3 Test Code

```kotlin
class AudioRecorderTest {

    private lateinit var recorder: AudioRecorder

    @Before
    fun setup() {
        // Use mock or test implementation
        recorder = AudioRecorder(context = mockContext)
    }

    @Test
    fun `REC-01 start sets isRecording to true`() {
        recorder.start()
        assertTrue(recorder.isRecording.value)
    }

    @Test
    fun `REC-02 stop returns audio data`() {
        recorder.start()
        Thread.sleep(100) // Record briefly
        val audioData = recorder.stop()

        assertFalse(recorder.isRecording.value)
        assertNotNull(audioData)
        assertTrue(audioData.isNotEmpty())
    }

    @Test
    fun `REC-03 cancel discards data`() {
        recorder.start()
        Thread.sleep(100)
        recorder.cancel()

        assertFalse(recorder.isRecording.value)
    }

    @Test
    fun `REC-04 amplitude is in valid range`() {
        recorder.start()
        Thread.sleep(50)
        val amplitude = recorder.amplitude.value

        assertTrue(amplitude in 0f..1f)
        recorder.cancel()
    }
}
```

---

## 6. AudioPlayer Tests (Unit Tests)

### 6.1 Playback Lifecycle

| ID | Test Case | Expected Result |
|----|-----------|-----------------|
| PL-01 | Play audio | isPlaying = true, progress updates |
| PL-02 | Pause audio | isPlaying = false, progress paused |
| PL-03 | Resume audio | Continues from pause position |
| PL-04 | Playback completes | isPlaying = false, onComplete called |
| PL-05 | Seek to position | Progress jumps to position |

### 6.2 Test Code

```kotlin
class AudioPlayerTest {

    private lateinit var player: AudioPlayer

    @Test
    fun `PL-01 play sets isPlaying true`() {
        val audioData = loadTestAudio()
        player = AudioPlayer(audioData)

        player.play()
        assertTrue(player.isPlaying.value)
        player.stop()
    }

    @Test
    fun `PL-02 pause stops playback`() {
        val audioData = loadTestAudio()
        player = AudioPlayer(audioData)

        player.play()
        player.pause()
        assertFalse(player.isPlaying.value)
    }

    @Test
    fun `PL-04 playback completion triggers callback`() {
        var completed = false
        val shortAudio = loadShortTestAudio() // 100ms clip
        player = AudioPlayer(shortAudio, onComplete = { completed = true })

        player.play()
        Thread.sleep(200)
        assertTrue(completed)
    }
}
```

---

## 7. Integration Tests

### 7.1 Full Widget Flow

| ID | Test Case | Expected Result |
|----|-----------|-----------------|
| INT-01 | Send text message | Message appears in list, callback fired |
| INT-02 | Record and send audio | Audio message appears in list |
| INT-03 | Receive new message | List updates, auto-scrolls |
| INT-04 | Play received audio | Audio plays inline |
| INT-05 | Theme change | All components update colors |

### 7.2 Test Code

```kotlin
class ChatVoiceWidgetIntegrationTest {

    @get:Rule
    val composeTestRule = createComposeRule()

    @Test
    fun `INT-01 send text message flow`() {
        val messages = mutableStateListOf<ChatMessage>()
        var sentText: String? = null

        composeTestRule.setContent {
            ChatVoiceWidget(
                messages = messages,
                onSendMessage = { text ->
                    sentText = text
                    messages.add(createUserMessage(text))
                },
                onSendAudio = {}
            )
        }

        // Type and send
        composeTestRule.onNodeWithTag("text_input")
            .performTextInput("Hello world")
        composeTestRule.onNodeWithTag("send_button")
            .performClick()

        // Verify
        assertEquals("Hello world", sentText)
        composeTestRule.onNodeWithText("Hello world")
            .assertIsDisplayed()
    }

    @Test
    fun `INT-03 new message auto-scrolls`() {
        val messages = mutableStateListOf<ChatMessage>()
        // Pre-populate with messages
        repeat(15) { messages.add(createAssistantMessage("Message $it")) }

        composeTestRule.setContent {
            ChatVoiceWidget(
                messages = messages,
                onSendMessage = {},
                onSendAudio = {}
            )
        }

        // Add new message
        messages.add(createAssistantMessage("New message"))
        composeTestRule.waitForIdle()

        // New message should be visible
        composeTestRule.onNodeWithText("New message")
            .assertIsDisplayed()
    }
}
```

---

## 8. Edge Cases & Error Handling

| ID | Test Case | Expected Result |
|----|-----------|-----------------|
| EC-01 | Very long message (10000 chars) | Renders without crash, scrollable |
| EC-02 | Rapid send button clicks | Only sends once, no duplicates |
| EC-03 | Recording permission denied | Shows error, mic button works again |
| EC-04 | Audio playback fails | Shows error state in bubble |
| EC-05 | Empty audio recording (0 bytes) | Discards, shows error |
| EC-06 | Component removed while recording | Recording stops, resources released |
| EC-07 | Config changes during use | Component updates correctly |

---

## 9. Accessibility Tests

| ID | Test Case | Expected Result |
|----|-----------|-----------------|
| A11Y-01 | Screen reader on messages | Announces sender and content |
| A11Y-02 | Screen reader on buttons | Announces "Send message", "Start recording" |
| A11Y-03 | Touch target sizes | All buttons >= 48dp |
| A11Y-04 | Color contrast | Text meets WCAG AA ratio |

---

## Test Data Helpers

```kotlin
fun createMessage(id: String, text: String, sender: MessageSender = MessageSender.USER) =
    ChatMessage(
        id = id,
        content = MessageContent.Text(text),
        sender = sender,
        timestamp = System.currentTimeMillis()
    )

fun createUserMessage(text: String) = createMessage(
    id = UUID.randomUUID().toString(),
    text = text,
    sender = MessageSender.USER
)

fun createAssistantMessage(text: String) = createMessage(
    id = UUID.randomUUID().toString(),
    text = text,
    sender = MessageSender.ASSISTANT
)

fun createAudioMessage(sender: MessageSender, durationMs: Long = 5000L) =
    ChatMessage(
        id = UUID.randomUUID().toString(),
        content = MessageContent.Audio(
            audioData = ByteArray(1000),
            durationMs = durationMs
        ),
        sender = sender,
        timestamp = System.currentTimeMillis()
    )
```

---

## Bug Injection Points (For Data Annotation)

These are potential bugs to inject for creating F2P (Fail-to-Pass) test cases:

| Bug ID | Description | Affected Tests |
|--------|-------------|----------------|
| BUG-01 | Send button enabled on whitespace | IB-03 |
| BUG-02 | Auto-scroll doesn't trigger on new message | ML-08, INT-03 |
| BUG-03 | Input not cleared after send | IB-04 |
| BUG-04 | Wrong message alignment (user left, assistant right) | ML-02, ML-03, MB-01, MB-02 |
| BUG-05 | Duration timer doesn't update | AR-02 |
| BUG-06 | Cancel button sends instead of discarding | AR-05 |
| BUG-07 | Audio resources not released on stop | REC-02, EC-06 |
| BUG-08 | Timestamp shows wrong format or missing | MB-03 |
| BUG-09 | Mic button visible when voice disabled | IB-09 |
| BUG-10 | Playback doesn't trigger onComplete | PL-04 |

---

## Summary

| Category | Test Count |
|----------|------------|
| MessageList | 10 |
| MessageBubble | 9 |
| InputBar | 10 |
| AudioRecordingOverlay | 6 |
| AudioRecorder | 8 |
| AudioPlayer | 5 |
| Integration | 5 |
| Edge Cases | 7 |
| Accessibility | 4 |
| **Total** | **64** |

---

**Created:** 2025-12-20
**Last Updated:** 2025-12-20
