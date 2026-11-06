package org.monarch.assistant

import android.app.Notification
import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.Service
import android.content.Context
import android.content.Intent
import android.os.IBinder
import android.os.PowerManager
import android.util.Log

class MonarchVoiceService : Service() {

    private lateinit var powerManager: PowerManager

    override fun onCreate() {
        super.onCreate()
        powerManager = getSystemService(Context.POWER_SERVICE) as PowerManager
        startForegroundServiceNotification()
        Log.d("MonarchAI", "Monarch Voice Interaction & Autonomous Service Initialized.")
    }

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        val action = intent?.action
        if (action == "ACTION_POST_BOOT_GREETING") {
            triggerPostBootGreeting()
        }
        return START_STICKY
    }

    private fun triggerPostBootGreeting() {
        Log.i("MonarchAI", "Jarvis Greeting: सर, फ़ोन रीस्टार्ट हो गया है और सभी सिस्टम्स तैयार हैं। क्या आज मेरे लिए कोई काम है?")
        // SpeechSynthesis / TTS audio hook here to speak out via system audio channel
    }

    /**
     * Executes safe voice-authenticated reboot or shutdown
     */
    fun handlePowerAction(action: String, spokenPasscode: String, savedPasscode: String): Boolean {
        if (spokenPasscode != savedPasscode) {
            Log.w("MonarchAI", "Voice Passcode Mismatch! Power action denied.")
            return false
        }

        when (action.lowercase()) {
            "reboot" -> {
                Log.i("MonarchAI", "Rebooting device via verified voice passcode...")
                powerManager.reboot(null)
                return true
            }
            "shutdown" -> {
                Log.i("MonarchAI", "Shutting down device via verified voice passcode...")
                // Direct system shutdown call
                val shutdownIntent = Intent("com.android.internal.intent.action.REQUEST_SHUTDOWN").apply {
                    putExtra("android.intent.extra.KEY_CONFIRM", false)
                    flags = Intent.FLAG_ACTIVITY_NEW_TASK
                }
                startActivity(shutdownIntent)
                return true
            }
        }
        return false
    }

    private fun startForegroundServiceNotification() {
        val channelId = "monarch_voice_channel"
        val channelName = "Monarch AI Background Service"
        val manager = getSystemService(NotificationManager::class.java)
        val channel = NotificationChannel(channelId, channelName, NotificationManager.IMPORTANCE_LOW)
        manager.createNotificationChannel(channel)

        val notification = Notification.Builder(this, channelId)
            .setContentTitle("Monarch AI")
            .setContentText("Autonomous System Layer Active")
            .setSmallIcon(android.R.drawable.ic_btn_speak_now)
            .build()

        startForeground(1001, notification)
    }

    override fun onBind(intent: Intent?): IBinder? = null
}
