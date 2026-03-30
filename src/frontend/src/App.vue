<script setup lang="ts">
import { ref } from "vue";

const events = ref<string[]>([]);
const message = ref("");
const ws = new WebSocket("ws://localhost:8000/ws");

ws.onmessage = (event) => {
  events.value.unshift(event.data);
};

function sendEvent() {
  if (!message.value.trim()) return;
  ws.send(message.value);
  message.value = "";
}
</script>

<template>
  <main style="font-family: sans-serif; margin: 2rem">
    <h1>Incident Horizon</h1>
    <input v-model="message" placeholder="Post incident update" />
    <button @click="sendEvent">Send</button>
    <ul>
      <li v-for="(e, i) in events" :key="i">{{ e }}</li>
    </ul>
  </main>
</template>
