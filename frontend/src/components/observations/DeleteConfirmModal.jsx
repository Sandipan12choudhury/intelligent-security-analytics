import { FaExclamationTriangle, FaSpinner } from "react-icons/fa";

import "./DeleteConfirmModal.css";

export default function DeleteConfirmModal({

    count,

    deleting,

    onConfirm,

    onCancel

}) {

    return (

        <div className="delete-confirm-overlay" onClick={onCancel}>

            <div

                className="delete-confirm-modal"

                onClick={(e) => e.stopPropagation()}

            >

                <div className="delete-confirm-icon">

                    <FaExclamationTriangle />

                </div>

                <h3>Delete {count} Observation{count > 1 ? "s" : ""}?</h3>

                <p>

                    This will permanently remove {count === 1 ? "this observation" : "these observations"} from
                    the dataset and recalculate every analytics table.
                    This action cannot be undone.

                </p>

                <div className="delete-confirm-actions">

                    <button

                        className="cancel-btn"

                        onClick={onCancel}

                        disabled={deleting}

                    >

                        Cancel

                    </button>

                    <button

                        className="confirm-delete-btn"

                        onClick={onConfirm}

                        disabled={deleting}

                    >

                        {

                            deleting ? (

                                <>
                                    <FaSpinner className="spin-icon" />
                                    Deleting...
                                </>

                            ) : (

                                "Yes, Delete"

                            )

                        }

                    </button>

                </div>

            </div>

        </div>

    );

}
