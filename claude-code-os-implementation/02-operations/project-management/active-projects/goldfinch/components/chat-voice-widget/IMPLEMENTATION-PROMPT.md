# Chat Voice Widget - Implementation Prompt

## Task

Build a reusable **ChatVoiceWidget** component in Kotlin/Jetpack Compose that provides a complete chat interface with voice recording capabilities. This component should be generic, backend-agnostic, and embeddable in any Android application.

---

## Requirements

### Core Functionality

1. **Message Display**
   - Display a scrollable list of chat messages
   - Support two sender types: USER and ASSISTANT
   - User messages: right-aligned, primary color bubble
   - Assistant messages: left-aligned, secondary color bubble
   - Show timestamps on each message
   - Auto-scroll to the newest message when new messages arrive
   - Handle empty state gracefully

2. **Text Input**
   - Multi-line text input field that expands as user types
   - Send button that is only enabled when text is present
   - Clear input field after sending
   - Support keyboard "Enter" to send (configurable)

3. **Voice Recording**
   - Microphone button to initiate voice recording
   - Request and handle RECORD_AUDIO permission
   - Show recording overlay with:
     - Recording duration timer (MM:SS format)
     - Visual waveform/amplitude indicator
     - Stop button (sends the recording)
     - Cancel button (discards the recording)
   - Convert recorded audio to ByteArray for transmission

4. **Audio Playback**
   - Display audio messages with playback controls
   - Play/pause toggle button
   - Progress bar showing playback position
   - Duration display
   - Handle audio focus properly

5. **Theming**
   - Accept a ChatTheme configuration for colors
   - Support light and dark theme presets
   - Allow custom color overrides

---

## API Specification

### Main Composable

```kotlin
@Composable
fun ChatVoiceWidget(
    messages: List<ChatMessage>,
    onSendMessage: (String) -> Unit,
    onSendAudio: (ByteArray) -> Unit,
    modifier: Modifier = Modifier,
    config: ChatVoiceConfig = ChatVoiceConfig()
)
```

### Data Models

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
}

enum class MessageSender { USER, ASSISTANT }

enum class MessageStatus { SENDING, SENT, ERROR }

data class ChatVoiceConfig(
    val theme: ChatTheme = ChatTheme.Default,
    val enableVoice: Boolean = true,
    val placeholder: String = "Type a message...",
    val showTimestamps: Boolean = true,
    val enterToSend: Boolean = false
)

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
        val Default: ChatTheme  // Light theme colors
        val Dark: ChatTheme     // Dark theme colors
    }
}
```

---

## Component Structure

```
ChatVoiceWidget (container)
├── MessageList
│   └── MessageBubble (repeated)
│       ├── TextContent OR
│       └── AudioContent (with AudioPlayer)
├── InputBar
│   ├── TextField
│   ├── MicrophoneButton
│   └── SendButton
└── AudioRecordingOverlay (conditional modal)
    ├── DurationTimer
    ├── WaveformVisualizer
    ├── StopButton
    └── CancelButton
```

---

## Implementation Details

### MessageList
- Use `LazyColumn` for efficient rendering of large message lists
- Maintain scroll state with `rememberLazyListState()`
- Use `LaunchedEffect` to auto-scroll when messages list changes
- Reverse layout so newest messages appear at bottom

### MessageBubble
- Use `Row` with `Arrangement.Start` or `Arrangement.End` based on sender
- Apply `clip(RoundedCornerShape(...))` for bubble shape
- Different corner radii for user vs assistant bubbles
- Padding and margin for visual spacing

### InputBar
- Use `TextField` with `OutlinedTextFieldDefaults` or custom styling
- `IconButton` for microphone and send actions
- Animate button states (enabled/disabled, recording active)

### AudioRecorder
- Use Android's `MediaRecorder` or `AudioRecord` API
- Sample rate: 44100 Hz (or 16000 Hz for speech)
- Channel: MONO
- Encoding: PCM 16-bit
- Provide amplitude readings for waveform visualization
- Output as WAV format (simple header + PCM data)

### AudioPlayer
- Use `MediaPlayer` or `ExoPlayer` for playback
- Track playback progress with coroutine-based polling
- Handle audio focus with `AudioManager`
- Release resources properly in `DisposableEffect`

---

## Constraints

1. **No Backend Coupling**: The component must not make any network calls. It receives messages and emits events via callbacks.

2. **Permission Handling**: The component should check for and request RECORD_AUDIO permission, but the host app is responsible for declaring it in the manifest.

3. **Lifecycle Awareness**: Audio recording and playback must properly handle lifecycle events (pause, stop on backgrounding).

4. **Memory Efficiency**: Audio data should be handled efficiently. Consider streaming for long recordings.

5. **Accessibility**: Include content descriptions for all interactive elements.

---

## Deliverables

1. `ChatVoiceWidget.kt` - Main composable
2. `MessageList.kt` - Message list component
3. `MessageBubble.kt` - Individual message display
4. `InputBar.kt` - Text input and action buttons
5. `AudioRecordingOverlay.kt` - Recording UI
6. `AudioPlayer.kt` - Playback component
7. `AudioRecorder.kt` - Recording logic
8. `Models.kt` - Data classes (ChatMessage, MessageContent, etc.)
9. `ChatTheme.kt` - Theme configuration

---

## Example Usage

```kotlin
class ChatViewModel : ViewModel() {
    private val _messages = MutableStateFlow<List<ChatMessage>>(emptyList())
    val messages: StateFlow<List<ChatMessage>> = _messages.asStateFlow()

    fun sendTextMessage(text: String) {
        val message = ChatMessage(
            id = UUID.randomUUID().toString(),
            content = MessageContent.Text(text),
            sender = MessageSender.USER,
            timestamp = System.currentTimeMillis()
        )
        _messages.value = _messages.value + message
        // Send to backend...
    }

    fun sendAudioMessage(audioData: ByteArray) {
        // Similar implementation for audio
    }
}

@Composable
fun ChatScreen(viewModel: ChatViewModel = viewModel()) {
    val messages by viewModel.messages.collectAsState()

    ChatVoiceWidget(
        messages = messages,
        onSendMessage = viewModel::sendTextMessage,
        onSendAudio = viewModel::sendAudioMessage,
        config = ChatVoiceConfig(
            theme = ChatTheme.Dark,
            enableVoice = true,
            placeholder = "Ask me anything..."
        )
    )
}
```

---

## Success Criteria

- [ ] Messages display correctly with proper alignment and styling
- [ ] Text input accepts multi-line input and sends on button press
- [ ] Voice recording starts, shows duration, visualizes amplitude
- [ ] Recording can be stopped (sends) or cancelled (discards)
- [ ] Audio messages can be played back with progress
- [ ] Theme colors are applied consistently
- [ ] Component handles empty state
- [ ] Component handles permission denial gracefully
- [ ] No memory leaks from audio resources
