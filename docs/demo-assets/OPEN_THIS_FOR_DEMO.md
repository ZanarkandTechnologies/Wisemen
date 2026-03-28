# OPEN THIS FOR DEMO

This is the simple human guide for running the demo.

If you are nervous, use this file.

---

# 1. What website do I go to?

Open this in your browser:

- `http://localhost:3000`

That is the main website.

If the website is slow or weird, use these backup files instead:

- `docs/demo-assets/fallback-artifacts/report-fallback.html`
- `docs/demo-assets/fallback-artifacts/interaction-fallback.html`

And keep this picture ready too:

- `docs/demo-assets/fallback-artifacts/screens/home.png`

---

# 2. What files do I put into the website?

On the home page, there is an upload area.

Upload **these 2 markdown files together**:

1. `docs/demo-assets/battery-factory-scenario.md`
2. `docs/demo-assets/battery-kg-quick-seed.md`

Then, in the text box / prompt box, paste the contents of:

3. `docs/demo-assets/primary-shock-prompt.md`

That is the main demo input.

## In very simple words

You are giving the system:

- one factory story
- one helper file with important companies and supply-chain facts
- one shock event

So the machine has enough information to tell a good story.

---

# 3. What should I expect to see?

## Stage A — Home page

### What you do
- go to `http://localhost:3000`
- upload the 2 markdown files
- paste the shock prompt
- click the button to start

### What you should see
- files listed in the upload area
- a prompt in the text box
- a start button

### What this means
You have given the app the factory and the shock.

---

## Stage B — Graph building / setup

### What you should see
- loading
- progress
- graph-like or setup-like screens

### What this means
The app is building the supply graph and preparing the simulation.

### What to say
> We are turning the factory and its supply chain into a knowledge graph, so the system can reason about what depends on what.

---

## Stage C — Stakeholder setup

### What you should see
- lists of companies / stakeholders / setup information
- maybe profile generation or configuration

### What this means
The system is creating the important actors in the supply chain.

### What to say
> Now the system knows who the important players are: suppliers, logistics, regulators, customers, and the factory itself.

---

## Stage D — Simulation run

### What you should see
- a run screen
- activity
- maybe timeline or progress

### What this means
The system is simulating how the shock moves through the network.

### What to say
> Now it is simulating the chain reaction: where the delay starts, where risk builds up, and how the factory gets squeezed.

---

## Stage E — Report / brief

### What you should see
You want to find these 4 things:

1. the **failure chain**
2. the **most constrained node**
3. the **estimated disruption window**
4. the **recommended actions**

### What this means
This is the payoff.

### What to say
> This is the operational risk brief. It tells us what breaks first, where the bottleneck is, how urgent it is, and what to do next.

---

## Stage F — Interaction / trust moment

### What you should see
- a place to ask questions
- or an interaction screen

### What this means
You can ask the system why the risk got worse.

### What to say
> This is the trust moment. We can ask the system why the risk becomes critical so fast, and it ties the answer back to the same failure chain.

---

# 4. What exact files do I use if the website breaks?

If the live app gets weird, stop trying to be fancy.

Use these files in this order:

1. `docs/demo-assets/fallback-artifacts/screens/home.png`
2. `docs/demo-assets/fallback-artifacts/report-fallback.html`
3. `docs/demo-assets/fallback-artifacts/interaction-fallback.html`

That is your safe demo path.

---

# 5. What do I say in the demo?

Use this simple version:

> We built Miro Supply.  
> We load a battery factory, inject a supply shock, build the supply graph, simulate the cascade, and generate an operational risk brief.  
> The brief shows what breaks first, the bottleneck, the disruption window, and what actions buy time.  
> Then we interrogate the system to explain why the risk escalated.

---

# 6. What should I NOT do?

Do not say:

- exact forecast
- guaranteed prediction
- perfect accuracy
- just a dashboard

Say instead:

- operational risk brief
- estimated disruption window
- constrained node
- mitigation actions
- decision support

---

# 7. If I only remember one thing, what is it?

Remember this:

## Upload these:

- `battery-factory-scenario.md`
- `battery-kg-quick-seed.md`

## Paste this:

- `primary-shock-prompt.md`

## Main website:

- `http://localhost:3000`

## Safe fallback:

- `home.png`
- `report-fallback.html`
- `interaction-fallback.html`

---

# 8. One last tiny checklist

- [ ] Open `http://localhost:3000`
- [ ] Upload:
  - [ ] `battery-factory-scenario.md`
  - [ ] `battery-kg-quick-seed.md`
- [ ] Paste:
  - [ ] `primary-shock-prompt.md`
- [ ] Start the run
- [ ] Show the brief
- [ ] Show the interaction
- [ ] If anything is weird, switch to fallback files
