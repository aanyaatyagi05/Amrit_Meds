const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());
app.use(express.static('public'));

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/amritmeds', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define Schemas
const customerSchema = new mongoose.Schema({
  mobile: String,
  email: String,
});

const medicineSchema = new mongoose.Schema({
  name: String,
  category: String,
});

const Customer = mongoose.model('Customer', customerSchema);
const Medicine = mongoose.model('Medicine', medicineSchema);

// Routes
app.post('/generate-otp', async (req, res) => {
  const { mobile, email } = req.body;
  const customer = new Customer({ mobile, email });
  await customer.save();

  // Simulate OTP generation
  res.json({ success: true });
});

app.get('/search', async (req, res) => {
  const query = req.query.query;
  const results = await Medicine.find({ name: { $regex: query, $options: 'i' } });
  res.json(results);
});

// Start Server
app.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});



