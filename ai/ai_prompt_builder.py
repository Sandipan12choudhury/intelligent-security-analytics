"""
==============================================================================
AI Prompt Builder

Purpose
-------
Constructs professional prompts for the Large Language Model (LLM)
using the enterprise AIContext.

This module DOES NOT:

    • Read Excel datasets
    • Perform analytics
    • Call Gemini/OpenAI
    • Store AI responses

Its only responsibility is to transform AIContext into
a structured enterprise prompt.

Author
------
Sandipan Choudhury

==============================================================================

"""

from .context_models import AIContext

# =============================================================================
# System Role
# =============================================================================

SYSTEM_ROLE = """
You are an experienced Enterprise Cybersecurity Consultant,
IT Security Auditor and Security Architect.

You possess expertise in:

• Enterprise Security Assessments
• IT General Controls (ITGC)
• Database Security Reviews
• Digital Forensic Readiness Assessment (DFRA)
• Secure Network Architecture (SNA)
• Data Flow Architecture (DFA / DFD)
• Secure Software Development
• Risk Assessment
• Cybersecurity Compliance
• Information Security Governance

Generate responses that are:

• Technically accurate
• Business aligned
• Risk aware
• Executive friendly
• Professional
"""

# =============================================================================
# AI Reasoning Instructions
# =============================================================================

AI_REASONING_INSTRUCTIONS = """
When generating the response:

1. Use the enterprise context provided.

2. Use the enterprise analytics to understand
   business criticality and risk posture.

3. Use the enterprise knowledge repository
   whenever applicable.

4. Apply your own cybersecurity expertise
   and professional reasoning.

5. Follow industry best practices
   including OWASP, NIST, ISO 27001,
   CIS Controls and secure architecture principles.

6. Do NOT merely repeat the provided context.

7. Produce an original,
   professional,
   well-structured response.

8. If enterprise knowledge is incomplete,
   use your own expertise to bridge the gap
   while remaining consistent with the provided context.
"""

# =============================================================================
# Response Quality Requirements
# =============================================================================

RESPONSE_QUALITY_REQUIREMENTS = """
The generated response must:

1. Be technically accurate and factually consistent.

2. Maintain a professional enterprise audit tone.

3. Be concise while providing sufficient technical detail.

4. Avoid unnecessary repetition.

5. Avoid unsupported assumptions.

6. Use clear and grammatically correct language.

7. Be aligned with enterprise cybersecurity best practices.

8. Be practical and actionable whenever appropriate.

9. Maintain consistency with the provided enterprise context.

10. Use your own cybersecurity expertise to enhance the response without contradicting the enterprise context.

11. Do not fabricate facts, configurations, or evidence that are not supported by the provided context.

12. Produce a response suitable for inclusion in professional security assessment reports.
"""

# =============================================================================
# Supported AI Artifacts
# =============================================================================

SUPPORTED_ARTIFACTS = {

    "ROOT_CAUSE": {

        "task":
            "Generate the technical and business root cause.",

        "audience":
            "Security Auditor",

        "output":
            """
Provide 1–2 professional paragraphs explaining:

• Technical root cause

• Process or governance gaps

• Why the issue occurred

Avoid recommending solutions.
"""

    },

    "RECOMMENDATION": {

        "task":
            "Generate professional remediation recommendations.",

        "audience":
            "Application Owner",

        "output":
            """
Provide a numbered list of practical remediation actions.

Recommendations should be:

• Actionable

• Technically accurate

• Prioritized

• Enterprise suitable

Do not repeat the observation.
"""

    },

    "BUSINESS_IMPACT": {

        "task":
            "Generate business impact analysis.",

        "audience":
            "Business Stakeholders",

        "output":
            """
Explain:

• Operational impact

• Security impact

• Regulatory impact

• Financial or reputational impact

Write in professional business language.
"""

    },

    "EXECUTIVE_SUMMARY": {

        "task":
            "Generate an executive-level security summary.",

        "audience":
            "Senior Management",

        "output":
            """
Write a concise executive summary.

Focus on:

• Overall risk

• Business importance

• Required management attention

Avoid excessive technical detail.
"""

    },

    "RISK_JUSTIFICATION": {

        "task":
            "Justify the assigned security risk.",

        "audience":
            "Risk Committee",

        "output":
            """
Explain why the assigned risk level is appropriate.

Consider:

• Severity

• Business Criticality

• Enterprise Risk

• Compliance

Provide logical justification.
"""

    },

    "PREVENTIVE_CONTROL": {

        "task":
            "Generate preventive security controls.",

        "audience":
            "Security Team",

        "output":
            """
Provide preventive controls.

Include:

• Administrative controls

• Technical controls

• Monitoring controls

• Governance improvements
"""

    }

}

# =============================================================================
# Prompt Builder
# =============================================================================

def build_prompt(context: AIContext) -> str:

    """
    Constructs a complete enterprise prompt
    from the supplied AIContext.
    """

    artifact = SUPPORTED_ARTIFACTS[
        context.request.artifact_type
    ]

    prompt = f"""
{SYSTEM_ROLE}

======================================================================
TASK
======================================================================

{artifact["task"]}

Target Audience:

{artifact["audience"]}

======================================================================
ENTERPRISE CONTEXT
======================================================================

Application:
{context.application.application_name}

Department:
{context.application.department}

Business Criticality:
{context.application.business_criticality}

Technology Domain:
{context.application.business_domain}

======================================================================
OBSERVATION
======================================================================

Activity:
{context.identity.activity}

Severity:
{context.identity.severity}

Observation:

{context.identity.observation}

======================================================================
KNOWLEDGE CONTEXT
======================================================================

Control Objective:

{context.knowledge.control_objective}

Security Principle:

{context.knowledge.security_principle}

Reference Standard:

{context.knowledge.reference_standard}

Additional Context:

{context.knowledge.prompt_context}

======================================================================
ENTERPRISE ANALYTICS
======================================================================

Application Risk Score:
{context.analytics.application_risk_score}

Department Risk Score:
{context.analytics.department_risk_score}

Enterprise Risk Score:
{context.analytics.enterprise_risk_score}

Application Compliance:
{context.analytics.application_compliance}%

Department Compliance:
{context.analytics.department_compliance}%

Enterprise Compliance:
{context.analytics.enterprise_compliance}%

Executive Priority:
{context.executive.executive_priority}

======================================================================
USER REQUEST
======================================================================

{context.request.user_prompt}

======================================================================
AI REASONING INSTRUCTIONS
======================================================================

{AI_REASONING_INSTRUCTIONS}

======================================================================
EXPECTED OUTPUT FORMAT
======================================================================

{artifact["output"]}

======================================================================
RESPONSE QUALITY REQUIREMENTS
======================================================================

{RESPONSE_QUALITY_REQUIREMENTS}

"""

    return prompt

# =============================================================================
# Prompt Builder Validation
# =============================================================================

from .context_engine import build_context


def validate_prompt_builder():

    """
    Validates that the Prompt Builder can successfully
    construct a complete enterprise prompt.
    """

    print()

    print("=" * 80)
    print("Validating AI Prompt Builder...")
    print("=" * 80)

    try:

        context = build_context(

            observation_id="OBS-0001",

            artifact_type="ROOT_CAUSE",

            user_prompt="Generate a professional technical root cause."

        )

        prompt = build_prompt(context)

        assert len(prompt) > 0

        assert context.application.application_name in prompt

        assert context.identity.observation in prompt

        assert context.knowledge.control_objective in prompt

        assert "AI REASONING INSTRUCTIONS" in prompt

        print()

        print("AI Prompt Builder validation completed successfully.")

        return prompt

    except Exception as error:

        print()

        print("Prompt Builder Validation Failed.")

        raise error


# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":

    prompt = validate_prompt_builder()

    print()

    print("=" * 80)
    print("SAMPLE GENERATED PROMPT")
    print("=" * 80)

    print()

    print(prompt)

    print()

    print("=" * 80)
    print("BUILD SUMMARY")
    print("=" * 80)

    print("Prompt Sections Included : 9")
    print(f"Supported Artifacts      : {len(SUPPORTED_ARTIFACTS)}")
    print("Prompt Status            : Ready")

    print("=" * 80)