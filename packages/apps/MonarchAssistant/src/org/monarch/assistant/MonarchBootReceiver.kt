package org.monarch.assistant

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.util.Log

class MonarchBootReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        if (intent.action == Intent.ACTION_BOOT_COMPLETED || 
            intent.action == Intent.ACTION_LOCKED_BOOT_COMPLETED) {
            Log.d("MonarchAI", "Device boot completed. Triggering Jarvis Autonomous Greeting...")
            
            // Start voice service with post-boot greeting trigger
            val serviceIntent = Intent(context, MonarchVoiceService::class.java).apply {
                action = "ACTION_POST_BOOT_GREETING"
            }
            context.startForegroundService(serviceIntent)
        }
    }
}
