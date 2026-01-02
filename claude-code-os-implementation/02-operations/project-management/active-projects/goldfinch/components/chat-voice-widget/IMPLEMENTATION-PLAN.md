# Chat Voice Widget - Implementation Plan

**Component:** Generic Chat UI + Audio Collection
**Platform:** Kotlin Multiplatform (Android)
**Status:** Planning
**Priority:** P0 - First component to build

---

## Overview

A reusable chat widget that combines:
1. **Chat UI** - Message display, text input, conversation flow
2. **Audio Collection** - Record, stream, and playback voice

This is a single, embeddable widget that any app can drop in for AI assistant interaction.

---

## Architecture

```
┌─────────────────────────────────────────────┐
│              ChatVoiceWidget                │
├─────────────────────────────────────────────┤
│  ┌─────────────────────────────────────┐   │
│  │         MessageList                  │   │
│  │  ┌─────────────────────────────┐    │   │
│  │  │ MessageBubble (user)        │    │   │
│  │  │ MessageBubble (assistant)   │    │   │
│  │  │ MessageBubble (user)        │    │   │
│  │  │ ...                         │    │   │
│  │  └─────────────────────────────┘    │   │
│  └─────────────────────────────────────┘   │
│  ┌─────────────────────────────────────┐   │
│  │         InputBar                     │   │
│  │  [TextField        ] [🎤] [Send]    │   │
│  └─────────────────────────────────────┘   │
│  ┌─────────────────────────────────────┐   │
│  │    AudioRecordingOverlay (modal)    │   │
│  │    [Waveform] [Stop] [Cancel]       │   │
│  └─────────────────────────────────────┘   │
└─────────────────────────────────────────────┘
```

---

## Component Breakdown

### 1. ChatVoiceWidget (Container)
**Purpose:** Main composable that orchestrates all sub-components
**Responsibilities:**
- Manage overall state (messages, recording status)
- Coordinate between chat and audio components
- Expose configuration API to host app

**Public API:**
```kotlin
@Composable
fun ChatVoiceWidget(
    config: ChatVoiceConfig,
    onSendMessage: (String) -> Unit,
    onSendAudio: (ByteArray) -> Unit,
    messages: List<ChatMessage>,
    modifier: Modifier = Modifier
)

data class ChatVoiceConfig(
    val theme: ChatTheme = ChatTheme.Default,
    val enableVoice: Boolean = true,
    val placeholder: String = "Type a message...",
    val showTimestamps: Boolean = true
)
```

---

### 2. MessageList
**Purpose:** Scrollable list of chat messages
**Responsibilities:**
- Display messages in chronological order
- Auto-scroll to bottom on new messages
- Handle scroll state

**Features:**
- [ ] LazyColumn for efficient rendering
- [ ] Auto-scroll to newest message
- [ ] Pull-to-load-more (optional, for history)
- [ ] Empty state display

---

### 3. MessageBubble
**Purpose:** Individual message display
**Responsibilities:**
- Render message content (text, audio, or mixed)
- Style based on sender (user vs assistant)
- Show timestamp and status

**Variants:**
- **TextBubble** - Plain text message
- **AudioBubble** - Playable audio with waveform
- **LoadingBubble** - Typing indicator / thinking state

**Features:**
- [ ] User bubble (right-aligned, primary color)
- [ ] Assistant bubble (left-aligned, secondary color)
- [ ] Timestamp display
- [ ] Message status (sending, sent, error)
- [ ] Audio playback controls (for audio messages)

---

### 4. InputBar
**Purpose:** Text input and action buttons
**Responsibilities:**
- Text field for typing messages
- Send button (enabled when text present)
- Microphone button to trigger recording

**Features:**
- [ ] Multi-line text input with auto-expand
- [ ] Send button with enabled/disabled states
- [ ] Microphone button to start recording
- [ ] Keyboard handling (enter to send option)

---

### 5. AudioRecordingOverlay
**Purpose:** Modal UI during voice recording
**Responsibilities:**
- Show recording status and duration
- Display audio waveform visualization
- Provide stop/cancel controls

**Features:**
- [ ] Recording duration timer
- [ ] Live waveform visualization
- [ ] Stop button (sends audio)
- [ ] Cancel button (discards audio)
- [ ] Slide-to-cancel gesture (optional)

---

### 6. AudioPlayer (inline)
**Purpose:** Playback controls for audio messages
**Responsibilities:**
- Play/pause audio
- Show progress
- Display duration

**Features:**
- [ ] Play/pause toggle
- [ ] Progress bar with seek
- [ ] Duration display
- [ ] Waveform visualization (static)

---

## Data Models

```kotlin
data class ChatMessage(
    val id: String,
    val content: MessageContent,
    val sender: MessageSender,
    val timestamp: Long,
    val status: MessageStatus = MessageStatus.SENT
)

sealed class MessageContent {
    data class Text(val text: String) : MessageContent()
    data class Audio(
        val audioData: ByteArray,
        val durationMs: Long,
        val waveform: List<Float>? = null
    ) : MessageContent()
    data class TextAndAudio(
        val text: String,
        val audio: Audio
    ) : MessageContent()
}

enum class MessageSender { USER, ASSISTANT }

enum class MessageStatus { SENDING, SENT, ERROR }

data class ChatTheme(
    val userBubbleColor: Color,
    val assistantBubbleColor: Color,
    val userTextColor: Color,
    val assistantTextColor: Color,
    val backgroundColor: Color,
    val inputBackgroundColor: Color,
    val accentColor: Color
) {
    companion object {
        val Default = ChatTheme(...)
        val Dark = ChatTheme(...)
    }
}
```

---

## Audio Collection Implementation

### Recording Flow
```
User taps 🎤
    ↓
Check microphone permission
    ↓ (granted)
Show AudioRecordingOverlay
Start AudioRecorder
    ↓
Capture audio chunks
Update waveform visualization
Update duration timer
    ↓
User taps Stop
    ↓
Stop AudioRecorder
Encode audio (WAV or MP3)
    ↓
Call onSendAudio(audioData)
Hide overlay
Show audio message in chat
```

### AudioRecorder Class
```kotlin
class AudioRecorder {
    fun start()
    fun stop(): ByteArray
    fun cancel()
    fun getAmplitude(): Float  // For waveform
    fun getDuration(): Long

    val isRecording: StateFlow<Boolean>
    val amplitude: StateFlow<Float>
    val duration: StateFlow<Long>
}
```

### Platform Implementation (Android)
- Use `MediaRecorder` or `AudioRecord` API
- Request `RECORD_AUDIO` permission
- Output format: PCM → convert to WAV or stream raw

---

## Implementation Phases

### Phase 1: Static Chat UI (No Audio)
**Estimate:** 2-3 hours
**Goal:** Working chat interface with text only

- [ ] Create ChatVoiceWidget composable
- [ ] Implement MessageList with LazyColumn
- [ ] Implement MessageBubble (text only)
- [ ] Implement InputBar (text + send button)
- [ ] Wire up basic state management
- [ ] Add theming support

**Deliverable:** Chat UI that displays messages and accepts text input

---

### Phase 2: Audio Recording
**Estimate:** 3-4 hours
**Goal:** Record audio and attach to messages

- [ ] Implement AudioRecorder class
- [ ] Handle microphone permissions
- [ ] Create AudioRecordingOverlay UI
- [ ] Add waveform visualization
- [ ] Encode audio output
- [ ] Integrate with InputBar (mic button)

**Deliverable:** Can record voice and send as message

---

### Phase 3: Audio Playback
**Estimate:** 2-3 hours
**Goal:** Play back audio messages

- [ ] Create AudioPlayer component
- [ ] Implement playback controls
- [ ] Add progress tracking
- [ ] Create AudioBubble variant
- [ ] Handle audio focus

**Deliverable:** Can play audio messages inline

---

### Phase 4: Polish & Integration
**Estimate:** 2-3 hours
**Goal:** Production-ready component

- [ ] Loading states and animations
- [ ] Error handling and retry
- [ ] Accessibility (content descriptions)
- [ ] Documentation and usage examples
- [ ] Sample app demonstrating integration

**Deliverable:** Shippable component with docs

---

## File Structure

```
goldfinch/
└── components/
    └── chat-voice-widget/
        ├── IMPLEMENTATION-PLAN.md (this file)
        ├── src/
        │   ├── ChatVoiceWidget.kt
        │   ├── MessageList.kt
        │   ├── MessageBubble.kt
        │   ├── InputBar.kt
        │   ├── AudioRecordingOverlay.kt
        │   ├── AudioPlayer.kt
        │   ├── AudioRecorder.kt
        │   ├── models/
        │   │   ├── ChatMessage.kt
        │   │   ├── MessageContent.kt
        │   │   └── ChatTheme.kt
        │   └── util/
        │       ├── AudioEncoder.kt
        │       └── WaveformGenerator.kt
        └── sample/
            └── SampleChatScreen.kt
```

---

## Integration Example

```kotlin
// Host app usage
@Composable
fun MyAppScreen(viewModel: MyViewModel) {
    val messages by viewModel.messages.collectAsState()

    ChatVoiceWidget(
        config = ChatVoiceConfig(
            theme = ChatTheme.Dark,
            enableVoice = true,
            placeholder = "Ask me anything..."
        ),
        messages = messages,
        onSendMessage = { text ->
            viewModel.sendTextMessage(text)
        },
        onSendAudio = { audioData ->
            viewModel.sendAudioMessage(audioData)
        }
    )
}
```

---

## Dependencies

```kotlin
// build.gradle.kts
dependencies {
    // Compose
    implementation("androidx.compose.material3:material3:1.2.0")
    implementation("androidx.compose.foundation:foundation:1.6.0")

    // Audio (Android)
    // Uses built-in MediaRecorder/AudioRecord - no external deps

    // Optional: Audio encoding
    implementation("com.arthenica:ffmpeg-kit-audio:5.1")  // If MP3 encoding needed
}
```

---

## Open Questions

1. **Audio format:** WAV (simple, large) vs MP3 (compressed, needs encoding)?
2. **Streaming:** Send audio in real-time chunks or after recording stops?
3. **Max duration:** Limit recording length? (e.g., 60 seconds)
4. **Transcription preview:** Show text transcription while recording?

---

## Success Criteria

- [ ] Chat UI renders messages correctly
- [ ] Text input works (send button, keyboard)
- [ ] Voice recording captures audio
- [ ] Audio playback works inline
- [ ] Theming is customizable
- [ ] Component is reusable (no hardcoded dependencies)
- [ ] Documentation allows easy integration

---

**Created:** 2025-12-17
**Last Updated:** 2025-12-17
