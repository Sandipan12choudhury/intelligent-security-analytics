import pandas as pd
from pathlib import Path

# ============================================================
# USER MANAGEMENT OBSERVATION LIBRARY
# ============================================================

OBSERVATIONS = [

    {
        "Activity": "ITGC",
        "Domain": "User Management",
        "Observation": (
            "Review of quarterly user access recertification records "
            "indicated that privileged user accounts were excluded from "
            "the periodic access review process. Absence of periodic "
            "validation of privileged access may result in excessive "
            "privileges remaining assigned to users without business "
            "justification, increasing the risk of unauthorized "
            "activities remaining undetected."
        ),
        "Severity": "High"
    },

    {
        "Activity": "ITGC",
        "Domain": "User Management",
        "Observation": (
            "Review of user de-provisioning records identified instances "
            "where user accounts belonging to separated employees remained "
            "active beyond the defined revocation timelines. Delayed removal "
            "of user access increases the risk of unauthorized access to "
            "application resources by former personnel."
        ),
        "Severity": "High"
    },

    {
        "Activity": "ITGC",
        "Domain": "User Management",
        "Observation": (
            "Review of privileged account inventories and corresponding "
            "approval records indicated that periodic recertification of "
            "privileged user accounts was not performed. Lack of management "
            "oversight over privileged access may result in excessive or "
            "inappropriate access privileges remaining undetected."
        ),
        "Severity": "High"
    },

    {
        "Activity": "ITGC",
        "Domain": "User Management",
        "Observation": (
            "Review of user entitlement reports identified multiple users "
            "possessing access rights inconsistent with their current job "
            "responsibilities. Absence of periodic entitlement validation "
            "may lead to accumulation of excessive privileges and increase "
            "the likelihood of unauthorized transactions."
        ),
        "Severity": "High"
    },

    {
        "Activity": "ITGC",
        "Domain": "User Management",
        "Observation": (
            "Review of access governance reports indicated that dormant user "
            "accounts remained enabled within the application environment "
            "despite prolonged inactivity. Retention of inactive accounts "
            "increases the attack surface and may facilitate unauthorized "
            "access if such accounts are compromised."
        ),
        "Severity": "High"
    },

    {
        "Activity": "ITGC",
        "Domain": "User Management",
        "Observation": (
            "Review of administrative account inventories identified shared "
            "privileged user IDs being utilized by multiple personnel for "
            "administrative activities. Usage of shared accounts weakens "
            "accountability and may prevent accurate attribution of critical "
            "system activities during security investigations."
        ),
        "Severity": "High"
    },

    {
        "Activity": "ITGC",
        "Domain": "User Management",
        "Observation": (
            "Review of joiner-mover-leaver records indicated that user access "
            "rights associated with previous roles were retained following "
            "employee transfers. Failure to revoke obsolete access privileges "
            "may result in segregation of duties conflicts and unauthorized "
            "access to sensitive business functions."
        ),
        "Severity": "High"
    },

    {
        "Activity": "ITGC",
        "Domain": "User Management",
        "Observation": (
            "Review of user provisioning records identified instances where "
            "access was granted without documented approval from the "
            "designated application owner. Absence of formal authorization "
            "controls increases the risk of inappropriate access assignments "
            "and unauthorized use of application functionalities."
        ),
        "Severity": "High"
    },

    {
        "Activity": "ITGC",
        "Domain": "User Management",
        "Observation": (
            "Review of vendor access management records indicated that "
            "third-party user accounts were not subjected to periodic "
            "access reviews. Lack of oversight over external user access "
            "may result in unauthorized access remaining undetected and "
            "increase exposure to third-party security risks."
        ),
        "Severity": "High"
    },

    {
        "Activity": "ITGC",
        "Domain": "User Management",
        "Observation": (
            "Review of user access review evidences indicated that the "
            "scope of periodic access certification activities did not "
            "include service accounts and privileged technical accounts. "
            "Exclusion of critical account categories from review processes "
            "may result in unmanaged access privileges and increase the "
            "risk of unauthorized system activities."
        ),
        "Severity": "High"
    },

    {
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of user account inventories identified generic user IDs "
        "being utilized for business operations without documented ownership "
        "or accountability. Usage of generic accounts limits traceability of "
        "user activities and may hinder effective investigation of security incidents."
    ),
    "Severity": "High"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of user account repositories identified orphan accounts that "
        "were not mapped to active employees or authorized third-party personnel. "
        "Retention of orphan accounts increases the risk of unauthorized access "
        "remaining undetected within the application environment."
    ),
    "Severity": "High"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of emergency access management records indicated that activities "
        "performed through emergency access accounts were not subjected to periodic "
        "management review. Lack of oversight over emergency access usage may result "
        "in unauthorized privileged activities remaining undetected."
    ),
    "Severity": "High"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of service account inventories indicated that periodic access reviews "
        "were not performed for application service accounts. Absence of periodic "
        "validation of service account privileges may result in excessive access "
        "rights remaining assigned without business necessity."
    ),
    "Severity": "High"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of user entitlement reports identified segregation of duties conflicts "
        "where individual users possessed access rights enabling execution of "
        "conflicting business functions. Such conflicts increase the risk of "
        "fraudulent activities and unauthorized transactions."
    ),
    "Severity": "High"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of privileged access approval records identified instances where "
        "privileged access rights were granted without documented business "
        "justification. Absence of formal justification may result in assignment "
        "of unnecessary privileged access and increase security risk exposure."
    ),
    "Severity": "High"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of user access governance reports identified multiple dormant "
        "privileged accounts remaining active within the production environment. "
        "Retention of inactive privileged accounts increases the likelihood of "
        "unauthorized access if such accounts are compromised."
    ),
    "Severity": "High"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of vendor user inventories indicated that ownership of third-party "
        "accounts was not formally assigned to internal personnel. Absence of "
        "account ownership may limit accountability and weaken oversight over "
        "external user access."
    ),
    "Severity": "Medium"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of access certification reports indicated that periodic access "
        "review activities were performed manually without evidence of independent "
        "validation. Reliance on manual review processes may affect completeness "
        "and reliability of access governance activities."
    ),
    "Severity": "Medium"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of user entitlement review evidences indicated that application "
        "owners did not formally approve access review outcomes. Absence of "
        "management sign-off may limit accountability for access governance decisions."
    ),
    "Severity": "Medium"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of role assignment records identified user roles assigned directly "
        "to individual users instead of utilizing approved role-based access control "
        "structures. Direct assignment of privileges may result in inconsistent "
        "access management practices."
    ),
    "Severity": "Medium"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of user provisioning requests identified delays between approval "
        "and access provisioning activities. Lack of defined provisioning timelines "
        "may affect operational efficiency and access governance effectiveness."
    ),
    "Severity": "Medium"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of access matrix documentation indicated that role definitions "
        "had not been updated to reflect recent organizational changes. Outdated "
        "access matrices may result in inaccurate access assignments and ineffective "
        "access governance."
    ),
    "Severity": "Medium"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of temporary access records identified instances where temporary "
        "access privileges remained active beyond approved validity periods. Failure "
        "to revoke temporary access in a timely manner may result in continued "
        "unauthorized access."
    ),
    "Severity": "Medium"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of user access governance procedures indicated that frequency of "
        "periodic user access reviews was not formally defined. Absence of defined "
        "review frequencies may result in inconsistent execution of access governance activities."
    ),
    "Severity": "Medium"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of application user inventories identified duplicate user accounts "
        "assigned to individual personnel. Presence of duplicate accounts may "
        "complicate monitoring activities and weaken accountability mechanisms."
    ),
    "Severity": "Medium"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of access ownership records indicated that responsibility for "
        "periodic review of user access rights was not formally assigned. Lack "
        "of ownership may impact effectiveness of user access governance processes."
    ),
    "Severity": "Medium"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of role ownership documentation indicated that several business "
        "roles did not have designated role owners. Absence of role ownership "
        "may affect accountability for approval and review of access privileges."
    ),
    "Severity": "Low"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of user access governance procedures indicated that documented "
        "guidelines for user access reviews were not available. Lack of formal "
        "procedures may result in inconsistent execution of access governance activities."
    ),
    "Severity": "Low"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of user entitlement documentation indicated that supporting "
        "evidences for selected access assignments could not be provided during "
        "the review. Absence of supporting documentation may limit validation "
        "of access authorization controls."
    ),
    "Severity": "Low"
},
{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of joiner-mover-leaver process evidences identified instances "
        "where user access rights associated with previous responsibilities "
        "were retained following employee role transitions. Failure to remove "
        "obsolete access privileges may result in excessive access accumulation "
        "and increase the risk of unauthorized activities."
    ),
    "Severity": "High"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of privileged user monitoring reports indicated that activities "
        "performed through privileged accounts were not subjected to periodic "
        "independent review. Absence of oversight over privileged activities "
        "may result in unauthorized actions remaining undetected."
    ),
    "Severity": "High"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of user entitlement certification records indicated that "
        "certification activities were performed without validating current "
        "business requirements for assigned access privileges. Inadequate "
        "entitlement validation may result in excessive access rights being retained."
    ),
    "Severity": "High"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of access exception records identified privileged access "
        "exceptions that remained active beyond approved exception periods. "
        "Failure to periodically reassess access exceptions may result in "
        "unauthorized privileged access remaining undetected."
    ),
    "Severity": "High"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of maker-checker control matrices identified users possessing "
        "access rights enabling both initiation and approval of critical "
        "business transactions. Absence of effective segregation of duties "
        "controls increases the risk of fraudulent or unauthorized transactions."
    ),
    "Severity": "High"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of privileged access governance reports identified privileged "
        "accounts assigned directly to users without approval from designated "
        "business owners. Lack of appropriate authorization may result in "
        "inappropriate assignment of elevated privileges."
    ),
    "Severity": "High"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of application access inventories identified multiple accounts "
        "with privileged access rights that were not included within the "
        "periodic access recertification process. Exclusion of privileged "
        "accounts from review activities may result in unmanaged access risks."
    ),
    "Severity": "High"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of emergency access account usage records identified instances "
        "where post-usage reviews were not performed following emergency access "
        "utilization. Absence of post-event validation may result in misuse of "
        "emergency privileges remaining undetected."
    ),
    "Severity": "High"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of user access governance controls identified absence of "
        "periodic validation of access rights assigned to outsourced support "
        "personnel. Lack of oversight over third-party access may increase "
        "exposure to external security threats."
    ),
    "Severity": "High"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of privileged account ownership records identified privileged "
        "accounts without formally assigned accountable owners. Absence of "
        "ownership may weaken accountability and hinder effective access governance."
    ),
    "Severity": "High"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of access recertification schedules indicated that periodic "
        "user access reviews were not consistently performed within defined "
        "review timelines. Delays in recertification activities may result in "
        "inappropriate access remaining active for extended periods."
    ),
    "Severity": "Medium"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of role assignment governance processes identified absence of "
        "documented periodic reviews of business role definitions. Failure to "
        "review role structures periodically may result in outdated access models."
    ),
    "Severity": "Medium"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of access governance committee records indicated that user "
        "access related exceptions were not periodically reported to senior "
        "management. Lack of management visibility may affect timely risk remediation."
    ),
    "Severity": "Medium"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of application user inventories identified accounts assigned "
        "to inactive organizational units. Retention of such access privileges "
        "may affect effectiveness of user access governance processes."
    ),
    "Severity": "Medium"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of user entitlement management procedures identified absence "
        "of defined criteria for determining privileged access eligibility. "
        "Lack of formal eligibility requirements may result in inconsistent "
        "assignment of elevated privileges."
    ),
    "Severity": "Medium"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of access review evidences indicated that supporting artifacts "
        "for selected certification decisions were not retained. Absence of "
        "audit trails may limit validation of review effectiveness."
    ),
    "Severity": "Medium"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of user access governance metrics identified absence of "
        "formal monitoring over completion status of periodic access reviews. "
        "Lack of monitoring may affect timely execution of governance activities."
    ),
    "Severity": "Medium"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of access governance documentation indicated that compensating "
        "controls associated with identified access exceptions were not formally "
        "documented. Absence of compensating controls may increase residual risk exposure."
    ),
    "Severity": "Medium"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of role ownership records identified delays in periodic review "
        "and approval of business roles. Delayed governance activities may "
        "impact effectiveness of access management processes."
    ),
    "Severity": "Low"
},

{
    "Activity": "ITGC",
    "Domain": "User Management",
    "Observation": (
        "Review of user access governance procedures indicated that formal "
        "review criteria for access certification activities were not documented. "
        "Absence of standardized review criteria may result in inconsistent "
        "execution of access review processes."
    ),
    "Severity": "Low"
}

]

# ============================================================
# CREATE DATAFRAME
# ============================================================

df = pd.DataFrame(OBSERVATIONS)

# ============================================================
# SAVE TO EXCEL
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

output_file = (
    BASE_DIR /
    "dataset" /
    "observation_library.xlsx"
)

df.to_excel(
    output_file,
    index=False
)

print("\n===================================")
print("User Management Library Created")
print("===================================")

print(f"\nTotal Observations : {len(df)}")

print(f"\nOutput File:\n{output_file}")