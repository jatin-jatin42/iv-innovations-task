const express = require('express');
const http = require('http');
const { Server } = require('socket.io');

const app = express();
app.use(express.json());

const server = http.createServer(app);
const io = new Server(server, {
  cors: {
    origin: "*",
    methods: ["GET", "POST"]
  }
});

io.on('connection', (socket) => {
  console.log('Client connected:', socket.id);
  
  socket.on('disconnect', () => {
    console.log('Client disconnected:', socket.id);
  });
});

app.post('/notify', (req, res) => {
  const { po_id, status } = req.body;
  if (!po_id || !status) {
    return res.status(400).json({ error: "Missing PO ID or Status" });
  }
  
  // Emitting event to all connected clients
  io.emit('po_status_change', { po_id, status, timestamp: new Date() });
  
  res.status(200).json({ success: true, message: "Notification sent" });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Notification service running on port ${PORT}`);
});
