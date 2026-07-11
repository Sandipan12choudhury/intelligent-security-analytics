"""
==============================================================================
AI Context Engine

Purpose
-------
Collects enterprise information from all knowledge, data and analytics layers
and constructs a complete AIContext object.

This module DOES NOT:

    • Generate prompts
    • Call LLMs
    • Generate AI artifacts

Its only responsibility is to build the complete AI context.

Author
------
Sandipan Choudhury

==============================================================================
"""

from backend.dataset_manager import dataset_manager

from .context_models import (
    AIContext,
    IdentityContext,
    ApplicationContext,
    KnowledgeContext,
    AnalyticsContext,
    ExecutiveContext,
    RequestContext
)

# =============================================================================
# Load Enterprise Datasets
# =============================================================================

observation_df = dataset_manager.get_observation_library().copy()

repository_df = dataset_manager.get_ai_repository()

mapping_df = dataset_manager.get_observation_mapping()

application_df = dataset_manager.get_application_dataset()

application_analytics_df = dataset_manager.get_application_analytics()

department_analytics_df = dataset_manager.get_department_analytics()

activity_analytics_df = dataset_manager.get_activity_analytics()

enterprise_analytics_df = dataset_manager.get_enterprise_analytics()

# =============================================================================
# Lookup Functions
# =============================================================================

def _get_observation(observation_id: str):

    """
    Returns a single observation record.
    """

    record = observation_df.loc[

        observation_df["Observation ID"] == observation_id

    ]

    if record.empty:

        raise ValueError(

            f"Observation '{observation_id}' not found."

        )

    return record.iloc[0]


# -----------------------------------------------------------------------------


def _get_repository_record(observation_id: str):

    """
    Returns AI Repository record.
    """

    record = repository_df.loc[

        repository_df["Observation ID"] == observation_id

    ]

    if record.empty:

        raise ValueError(

            f"Repository record for '{observation_id}' not found."

        )

    return record.iloc[0]


# -----------------------------------------------------------------------------


def _get_mapping(observation_id: str):

    """
    Returns Observation → Application mapping.
    """

    record = mapping_df.loc[

        mapping_df["Observation ID"] == observation_id

    ]

    if record.empty:

        raise ValueError(

            f"Application mapping for '{observation_id}' not found."

        )

    return record.iloc[0]


# -----------------------------------------------------------------------------


def _get_application(application_id: str):

    """
    Returns Application Dataset record.
    """

    record = application_df.loc[

        application_df["Application ID"] == application_id

    ]

    if record.empty:

        raise ValueError(

            f"Application '{application_id}' not found."

        )

    return record.iloc[0]


# -----------------------------------------------------------------------------


def _get_application_analytics(application_id: str):

    """
    Returns Application Analytics record.
    """

    record = application_analytics_df.loc[

        application_analytics_df["Application ID"] == application_id

    ]

    if record.empty:

        raise ValueError(

            f"Application Analytics for '{application_id}' not found."

        )

    return record.iloc[0]


# -----------------------------------------------------------------------------


def _get_department_analytics(department: str):

    """
    Returns Department Analytics record.
    """

    record = department_analytics_df.loc[

        department_analytics_df["Department"] == department

    ]

    if record.empty:

        raise ValueError(

            f"Department Analytics for '{department}' not found."

        )

    return record.iloc[0]


# -----------------------------------------------------------------------------


def _get_activity_analytics(activity: str):

    """
    Returns Activity Analytics record.
    """

    record = activity_analytics_df.loc[

        activity_analytics_df["Activity"] == activity

    ]

    if record.empty:

        raise ValueError(

            f"Activity Analytics for '{activity}' not found."

        )

    return record.iloc[0]


# -----------------------------------------------------------------------------


def _get_enterprise_analytics():

    """
    Returns Enterprise Analytics record.
    """

    return enterprise_analytics_df.iloc[0]

# =============================================================================
# Build AI Context
# =============================================================================

def build_context(
    observation_id: str,
    artifact_type: str,
    user_prompt: str = "",
    regenerate: bool = False,
    response_version: int = 1
) -> AIContext:

    """
    Constructs a complete AIContext object by assembling
    information from all enterprise datasets.
    """

    # =========================================================================
    # Knowledge Layer
    # =========================================================================

    observation = _get_observation(
        observation_id
    )

    repository = _get_repository_record(
        observation_id
    )

    # =========================================================================
    # Data Layer
    # =========================================================================

    mapping = _get_mapping(
        observation_id
    )

    application = _get_application(
        mapping["Application ID"]
    )

    # =========================================================================
    # Analytics Layer
    # =========================================================================

    application_analytics = _get_application_analytics(
        application["Application ID"]
    )

    department_analytics = _get_department_analytics(
        application["Department"]
    )

    activity_analytics = _get_activity_analytics(
        observation["Activity"]
    )

    enterprise_analytics = _get_enterprise_analytics()

    # =========================================================================
    # Identity Context
    # =========================================================================

    identity_context = IdentityContext(

        observation_id=observation["Observation ID"],

        observation=observation["Observation"],

        activity=observation["Activity"],

        domain=observation["Domain"],

        severity=observation["Severity"]

    )

    # =========================================================================
    # Application Context
    # =========================================================================

    application_context = ApplicationContext(

        application_id=application["Application ID"],

        application_name=application["Application Name"],

        department=application["Department"],

        business_domain=application["Technology Domain"],

        business_criticality=application["Business Criticality"],

        application_type=application["Application Type"],

        environment=application["Environment"],

        status=application["Status"]

    )

    # =========================================================================
    # Knowledge Context
    # =========================================================================

    knowledge_context = KnowledgeContext(

        control_objective=repository["Control Objective"],

        security_principle=repository["Security Principle"],

        reference_standard=repository["Reference Standard"],

        keywords=repository["Keywords"],

        prompt_context=repository["Prompt Context"]

    )

    # =========================================================================
    # Analytics Context
    # =========================================================================

    analytics_context = AnalyticsContext(

        application_risk_score=application_analytics["Risk Score"],

        department_risk_score=department_analytics["Average Risk Score"],

        activity_risk_score=activity_analytics["Risk Score"],

        enterprise_risk_score=enterprise_analytics["Average Risk Score"],

        application_compliance=application_analytics["Compliance %"],

        department_compliance=department_analytics["Average Compliance %"],

        enterprise_compliance=enterprise_analytics["Average Compliance %"],

        application_rank=application_analytics["Risk Rank"],

        department_rank=department_analytics["Department Rank"],

        activity_rank=activity_analytics["Enterprise Rank"],

        enterprise_rank=1,

        risk_category=application_analytics["Risk Category"]

    )

    # =========================================================================
    # Executive Context
    # =========================================================================

    executive_context = ExecutiveContext(

        executive_priority=department_analytics["Executive Priority"],

        dominant_severity=department_analytics["Dominant Severity"],

        top_activity=department_analytics["Top Activity"],

        top_risk_application_id=department_analytics[
            "Highest Risk Application ID"
        ],

        top_risk_application_name=department_analytics[
            "Highest Risk Application Name"
        ],

        highest_risk_department=enterprise_analytics[
            "Highest Risk Department"
        ]

    )

    # =========================================================================
    # Request Context
    # =========================================================================

    request_context = RequestContext(

        artifact_type=artifact_type,

        user_prompt=user_prompt,

        regenerate=regenerate,

        response_version=response_version

    )

    # =========================================================================
    # Return Complete AI Context
    # =========================================================================

    return AIContext(

        identity=identity_context,

        application=application_context,

        knowledge=knowledge_context,

        analytics=analytics_context,

        executive=executive_context,

        request=request_context

    )

    
# =============================================================================
# Context Engine Validation
# =============================================================================

def validate_context_engine():

    """
    Validates that the Context Engine can successfully build
    an AIContext object using a sample observation.
    """

    print()

    print("=" * 80)
    print("Validating AI Context Engine...")
    print("=" * 80)

    try:

        # ---------------------------------------------------------------------
        # Use the first Observation ID from the repository
        # ---------------------------------------------------------------------

        sample_observation_id = repository_df.iloc[0]["Observation ID"]

        context = build_context(

            observation_id=sample_observation_id,

            artifact_type="ROOT_CAUSE"

        )

        # ---------------------------------------------------------------------
        # Basic Validation
        # ---------------------------------------------------------------------

        assert context.identity.observation_id == sample_observation_id

        assert context.application.application_id != ""

        assert context.knowledge.control_objective != ""

        assert context.analytics.application_risk_score >= 0

        assert context.executive.executive_priority != ""

        assert context.request.artifact_type == "ROOT_CAUSE"

        print()

        print("AI Context Engine validation completed successfully.")

        return context

    except Exception as error:

        print()

        print("Context Engine Validation Failed.")

        raise error


# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":

    context = validate_context_engine()

    print()

    print("=" * 80)
    print("SAMPLE AI CONTEXT")
    print("=" * 80)

    print()

    print("Identity")
    print("------------------------------")
    print(f"Observation ID : {context.identity.observation_id}")
    print(f"Observation    : {context.identity.observation}")
    print(f"Activity       : {context.identity.activity}")
    print(f"Severity       : {context.identity.severity}")

    print()

    print("Application")
    print("------------------------------")
    print(f"Application    : {context.application.application_name}")
    print(f"Department     : {context.application.department}")
    print(f"Criticality    : {context.application.business_criticality}")

    print()

    print("Knowledge")
    print("------------------------------")
    print(f"Control Obj.   : {context.knowledge.control_objective}")
    print(f"Reference Std. : {context.knowledge.reference_standard}")

    print()

    print("Analytics")
    print("------------------------------")
    print(f"App Risk       : {context.analytics.application_risk_score}")
    print(f"Dept Risk      : {context.analytics.department_risk_score}")
    print(f"Enterprise     : {context.analytics.enterprise_risk_score}")

    print()

    print("=" * 80)
    print("BUILD SUMMARY")
    print("=" * 80)

    print(f"Knowledge Sources Loaded   : 2")
    print(f"Data Sources Loaded        : 2")
    print(f"Analytics Sources Loaded   : 4")
    print(f"AI Context Status          : Ready")
    print("=" * 80)