<script>
  // No dynamic content needed for static homepage layout
</script>

<div class="homepage-container">
  <div class="homepage-top">
    <div class="main-heading">MediScribe</div>
    <div class="subtitle">Introducing an AI powered doctor's handwriting recognition model</div>
  </div>
  <div class="examples-row">
    <div class="example-box left-box">
      <div class="placeholder-content">
        <svg class="placeholder-icon" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#3b82f6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="4"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
        <div class="placeholder-text">Image Placeholder</div>
      </div>
    </div>
    <div class="arrow-container">
      <svg width="60" height="40" viewBox="0 0 60 40">
        <defs>
          <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
            <polygon points="0 0, 10 3.5, 0 7" fill="#3b82f6" />
          </marker>
        </defs>
        <line x1="0" y1="20" x2="50" y2="20" stroke="#3b82f6" stroke-width="3" marker-end="url(#arrowhead)" />
      </svg>
    </div>
    <div class="example-box right-box">
      <div class="placeholder-content">
        <svg class="placeholder-icon" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#3b82f6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="4"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
        <div class="placeholder-text">Image Placeholder</div>
      </div>
    </div>
  </div>
</div>

<style>
.homepage-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 1.5rem 1rem 2rem 1rem; /* reduced top padding */
  background: #f8fafc;
}

.homepage-top {
  background: #fff;
  border-radius: 18px;
  box-shadow: 0 2px 16px rgba(59,130,246,0.06);
  border: 1.5px solid #e3e9f7;
  padding: 3.5rem 2.5rem 2.5rem 2.5rem;
  margin-bottom: 2rem;
  max-width: 1100px;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  animation: fadeInTop 0.7s cubic-bezier(.39,.575,.565,1) both;
}

@keyframes fadeInTop {
  0% { opacity: 0; transform: translateY(-30px); }
  100% { opacity: 1; transform: translateY(0); }
}

.main-heading {
  font-size: 2.7rem;
  font-weight: 800;
  color: #3b82f6;
  margin-bottom: 1.1rem;
  letter-spacing: 1px;
  text-align: center;
  text-shadow: 0 2px 8px rgba(59,130,246,0.07);
}

.subtitle {
  font-size: 1.25rem;
  color: #4b5e7a;
  font-weight: 500;
  text-align: center;
  line-height: 1.5;
  max-width: 90%;
}

.examples-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  margin-top: 2rem;
}

.example-box {
  background: linear-gradient(135deg, #f0f4ff 0%, #e3e9f7 100%);
  color: #3b82f6;
  font-size: 1.25rem;
  font-weight: 600;
  padding: 2.5rem 3rem;
  border-radius: 22px;
  min-width: 380px;
  min-height: 260px;
  text-align: center;
  box-shadow: 0 4px 24px rgba(59,130,246,0.08), 0 1.5px 6px rgba(0,0,0,0.04);
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px dashed #b2b2b2;
  transition: box-shadow 0.2s, transform 0.2s;
}
.example-box:hover {
  box-shadow: 0 8px 32px rgba(59,130,246,0.16), 0 3px 12px rgba(0,0,0,0.08);
  transform: translateY(-4px) scale(1.03);
  border-color: #3b82f6;
}
.placeholder-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.placeholder-icon {
  margin-bottom: 0.7rem;
}
.placeholder-text {
  color: #3b82f6;
  font-size: 1.2rem;
  font-style: italic;
  font-weight: 700;
  letter-spacing: 0.5px;
}

.arrow-container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}

@media (max-width: 700px) {
  .examples-row {
    flex-direction: column;
    gap: 1.5rem;
  }
  .arrow-container {
    transform: rotate(90deg);
  }
}
</style> 