/* @odoo-module */
/* global document */
import {Component, onMounted, useState} from "@odoo/owl";
import {Dropdown} from "@web/core/dropdown/dropdown";
import {DropdownItem} from "@web/core/dropdown/dropdown_item";
import {registry} from "@web/core/registry";
import {useDiscussSystray} from "@mail/utils/common/hooks";
import {useService} from "@web/core/utils/hooks";
import {user} from "@web/core/user";
import {_t} from "@web/core/l10n/translation";

const systrayRegistry = registry.category("systray");
export class SignerMenuView extends Component {
    setup() {
        this.discussSystray = useDiscussSystray();
        this.orm = useService("orm");
        this.action = useService("action");
        this.watchSignRequests = useService("watchSignRequests");
        this.state = useState({
            sign_requests: this.watchSignRequests.sign_requests,
        });
        onMounted(async () => {
            await this.watchSignRequests.fetchSystraySigner();
        });
    }
    availableViews() {
        return [
            [false, "kanban"],
            [false, "list"],
            [false, "form"],
            [false, "activity"],
        ];
    }
    async onClickFilterButton(group) {
        // Hack to close dropdown
        document.body.click();
        const context = {};
        const views = this.availableViews();
        // Partner_id is removed from session in version 18.0
        // Importing user object which is the current user instead of session object
        this.action.doAction(
            {
                type: "ir.actions.act_window",
                name:
                    group && group.name && group.name !== "Undefined"
                        ? _t(group.name)
                        : _t("Documents to be Signed"),
                res_model: "sign.oca.request.signer",
                views,
                search_view_id: [false],
                domain: [
                    ["request_id.state", "=", "sent"],
                    ["partner_id", "child_of", [user.partnerId]],
                    ["signed_on", "=", false],
                ],
                context,
            },
            {
                clearBreadcrumbs: true,
            }
        );
    }
}

SignerMenuView.template = "sign_oca.SignerMenu";
SignerMenuView.components = {Dropdown, DropdownItem};
SignerMenuView.props = [];
export const systrayItem = {Component: SignerMenuView};
systrayRegistry.add("sign_oca.SignerMenuView", systrayItem, {sequence: 99});
