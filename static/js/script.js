
document.getElementById('loginForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const mobile = document.getElementById('mobile').value;
  const email = document.getElementById('email').value;

  // Simulate OTP generation
  const response = await fetch('/generate-otp', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ mobile, email }),
  });

  const data = await response.json();
  if (data.success) {
    document.getElementById('otpMessage').innerText = `OTP sent to ${email}`;
    window.location.href = '/home.html'; // Redirect to homepage
  } else {
    document.getElementById('otpMessage').innerText = 'Failed to generate OTP';
  }
});

// For Search Tool
function searchMedicine() {
  const query = document.getElementById('searchInput').value;
  fetch(`/search?query=${query}`)
    .then((response) => response.json())
    .then((data) => {
      alert(`Results: ${JSON.stringify(data)}`);
    })
    .catch((err) => console.error(err));
}
