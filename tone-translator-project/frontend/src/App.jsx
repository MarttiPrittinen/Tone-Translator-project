import { useState } from 'react'

const tones = [
  { value: 'formal', label: 'Formal' },
  { value: 'casual', label: 'Casual' },
  { value: 'friendly', label: 'Friendly' },
  { value: 'professional', label: 'Professional' },
  { value: 'pirate', label: 'Pirate' },
  { value: 'shakespeare', label: 'Shakespeare' },
]

export default function App() {
  const [text, setText] = useState('Can you send me the report today?')
  const [tone, setTone] = useState('formal')
  const [result, setResult] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const handleSubmit = async (event) => {
    event.preventDefault()
    setLoading(true)
    setError('')
    setResult('')

    try {
      const response = await fetch('http://localhost:8000/translate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text, tone }),
      })

      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.detail || 'Something went wrong.')
      }

      setResult(data.result)
    } catch (err) {
      setError(err.message || 'Request failed.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="page">
      <div className="card">
        <h1>Tone Translator</h1>
        <p className="subtitle">Rewrite text with a different tone using React + FastAPI + Gemini API.</p>

        <form onSubmit={handleSubmit}>
          <label htmlFor="text">Text</label>
          <textarea
            id="text"
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Write or paste text here..."
            rows="8"
            required
          />

          <label htmlFor="tone">Tone</label>
          <select id="tone" value={tone} onChange={(e) => setTone(e.target.value)}>
            {tones.map((item) => (
              <option key={item.value} value={item.value}>
                {item.label}
              </option>
            ))}
          </select>

          <button type="submit" disabled={loading || !text.trim()}>
            {loading ? 'Translating...' : 'Translate'}
          </button>
        </form>

        {error && (
          <div className="output error">
            <h2>Error</h2>
            <p>{error}</p>
          </div>
        )}

        {result && (
          <div className="output">
            <h2>Result</h2>
            <p>{result}</p>
          </div>
        )}
      </div>
    </div>
  )
}
